package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break

object P13 extends App {

  case class Grid(lines: Array[String])

  def parseFile(): List[Grid] = {
    val lb :mutable.ListBuffer[String] = mutable.ListBuffer()
    val grids : mutable.ListBuffer[Grid] = mutable.ListBuffer()
    Source.fromFile(filename).getLines().map {
      line =>
        if (line.isBlank) {
          grids.append(Grid(lb.toList.toArray))
          lb.clear
        } else lb.append(line)
    }.toList
    grids.append(Grid(lb.toList.toArray)).toList
  }

  def parseFileFoldLeft(): List[Grid] = {
    case class Acc(grids: List[Grid], lines: List[String])
    val ac = Source.fromFile(filename).getLines().foldLeft(Acc(List(), List())) {
      (acc, line) =>
        if (line.isBlank) {
          Acc(acc.grids :+ Grid(acc.lines.toArray), List())
        } else {
          Acc(acc.grids, acc.lines :+ line)
        }
    }
    ac.grids :+ Grid(ac.lines.toArray)
  }

  def part1(grids: List[Grid]): Int = {
    grids.map(findReflection).sum
  }

  def part2(grids: List[Grid]): Int = {
    grids.map(findReflectionSmudged).sum
  }

  def findReflection(grid: Grid): Int = {
    val above = findReflectionHelper(grid.lines)
    if (above > 0) return 100*above
    val cols: Array[String] = grid.lines.map(x => x.toCharArray).transpose.map(l => new String(l))
    val r = findReflectionHelper(cols)
    if (r == -1) throw Exception ("oops " + grid.lines)
    r
  }

  def findReflectionSmudged(grid: Grid): Int = {
    val above = findReflectionSmudgedHelper(grid.lines)
    if (above > 0) return 100 * above
    val cols: Array[String] = grid.lines.map(x => x.toCharArray).transpose.map(l => new String(l))
    val r = findReflectionSmudgedHelper(cols)
    if (r == -1) throw Exception("oops " + grid.lines)
    r
  }

  def findReflectionHelper(lines: Array[String]): Int = {
    val matches = lines.zipWithIndex.sliding(2).filter { case Array(a, b) => a._1.equals(b._1) }.map(a => (a.head._2, a.last._2))
      .filter { case (l1, l2) => {
        var i = 1
        var allMatch = true
        while (l1 - i >= 0 && l2 + i < lines.length) {
          if (!lines(l1 - i).equals(lines(l2 + i))) {
            allMatch = false
            i = l1 + 1 // hack to terminate loop
          } else i += 1
        }
        allMatch
      }
      }.toList
    if (matches.nonEmpty) return matches.head._2
    -1
  }

  def equalWithSmudge(l1: String, l2: String): Boolean = {
    l1.zip(l2).count((c1, c2) => !c1.equals(c2)) == 1
  }
  def findReflectionSmudgedHelper(lines: Array[String]): Int = {
    val matches = lines.zipWithIndex.combinations(2).filter { case Array((s1, l1), (s2 ,l2)) =>  (l2 - l1) % 2 == 1 && equalWithSmudge(s1, s2) }
      .map { case Array((s1, l1), (s2,l2)) =>
        val line1 = (l2 + l1) / 2
        val line2 = line1 + 1
        var i = 0
        var allMatch = true
        while (allMatch && line1 - i >= 0 && line2 + i < lines.length) {
          if (line1-i != l1 && !lines(line1 - i).equals(lines(line2 + i))) {
            allMatch = false
            i = line1 + 1 // hack to terminate loop
          } else i += 1
        }
        if (allMatch) line2 else -1
      }.filter(_ != -1).toList
    if (matches.nonEmpty) return matches.head
    -1
  }

// 39129 too high

  val filename = "input/p13.txt"
  try {
    val grids = parseFileFoldLeft()
    //println(part1(grids))
    println(part2(grids))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
