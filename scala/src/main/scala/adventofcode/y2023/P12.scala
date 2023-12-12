package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break

object P12 extends App {

  case class Line(springs: String, damaged: List[Int])

  def parseFile(): List[Line] = {
    Source.fromFile(filename).getLines().map {
      case s"$springs $damaged" => Line(springs, damaged.split(',').map(_.toInt).toList)
    }.toList
  }

  def part1(lines: List[Line]): Int = {
   lines.zipWithIndex.map((l, index) => {
     handle(l.springs, l.damaged)
   }).sum
  }

  def part2(lines: List[Line]): Long = {
    lines.zipWithIndex.map((l, index) => {
      val s = s"${l.springs}?${l.springs}?${l.springs}?${l.springs}?${l.springs}"
      val biglist = List(l.damaged, l.damaged, l.damaged, l.damaged, l.damaged).flatten.toList
      println("i=" + index)
      val cache = mutable.Map[(String, List[Int]), Long]()
      dfs(s, biglist, cache)
    }).sum
  }

  def handle(springs: String, damaged: List[Int]): Int = {
    if (!springs.contains("?")) return if isPossible(springs, damaged) then 1 else 0
    var s1 = springs.replaceFirst("\\?", ".")
    var s2 = springs.replaceFirst("\\?", "#")
    var sum = 0;
    sum += handle(s1, damaged)
    sum += handle(s2, damaged)
    sum
  }

  def dfs(springs: String, damaged: List[Int], cache : mutable.Map[(String, List[Int]), Long]): Long = {
    if !isPossible(springs, damaged) then return 0
    if (!springs.contains("?")) return 1

    if (cache.contains((springs, damaged))) return cache((springs, damaged))

    var maybeFirst = """^\.*#+\.""".r.findFirstMatchIn(springs)
    if (maybeFirst.nonEmpty) {
      var end = maybeFirst.get.end
      return dfs(springs.substring(end), damaged.slice(1, damaged.length), cache)
    }

    var s1 = springs.replaceFirst("\\?", ".")
    var s2 = springs.replaceFirst("\\?", "#")
    var sum = 0L;
    sum += dfs(s1, damaged, cache)
    sum += dfs(s2, damaged, cache)
    cache.put((springs, damaged), sum)
    sum
  }

  def isPossible(springs: String, damaged: List[Int]): Boolean = {
    if (damaged.isEmpty) return !springs.contains("#")
    val buf = mutable.ListBuffer[Int]()
    var numDamaged = 0
    springs.zipWithIndex.foreach((c,index) => {
      if (c == '#') numDamaged += 1
      if (c == '.') {
        if (numDamaged > 0) {
          buf.append(numDamaged)
        }
        numDamaged = 0
      }
      if (c == '?') {
        if !buf.toList.equals(damaged.slice(0, buf.length)) then return false
        if (numDamaged > 0) return if buf.length > damaged.length-1 then false else numDamaged <= damaged(buf.length)

        val remaining = damaged.slice(buf.length, damaged.length).sum
        val remainingMax = springs.substring(index).replace('?', '#').count(x => x == '#')

        return remaining <= remainingMax
      }
    })
    if (numDamaged > 0) buf.append(numDamaged)
    damaged.equals(buf.toList)
  }

  val filename = "input/p12.txt"
  try {
    val lines = parseFile()
    println(part2(lines))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
