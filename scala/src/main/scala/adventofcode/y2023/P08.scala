package adventofcode.y2023

import scala.io.Source

object P08 extends App {

  case class Guide(directions: String, map: Map[String, (String, String)], aNodes: Seq[String])

  def parseFile(): Guide = {
    val itr: Iterator[String] = Source.fromFile(filename).getLines()
    val directions = itr.next
    itr.next
    val map = itr.map {
      case s"$a = ($b, $c)" => a -> (b, c)
    }.toMap
    val aNodes = map.keys.filter(_.endsWith("A"))
    Guide(directions, map, aNodes.toSeq)
  }

  def part1(guide: Guide) :Int = {
    var steps: Int = 0
    var cur: String = "AAA"
    while (!cur.equals("ZZZ")) {
      guide.directions.foreach( d => {
        val tuple = guide.map(cur)
        val next = if d == 'L' then tuple._1 else tuple._2
        cur = next
        steps += 1
        if (cur.equals("ZZZ")) return steps
      })
    }
    steps
  }

  def lcmOfArray(numbers: Array[Int]): Long = {
    numbers.map(x => x.toLong).reduce(lcm)
  }

  def lcm(a: Long, b: Long): Long = {
    (a * b) / gcd(a, b)
  }

  def gcd(a: Long, b: Long): Long = {
    if (b == 0) a else gcd(b, a % b)
  }

  def part2(guide: Guide): Long = {
    def finished(a : Array[String]) : Boolean = {
      a.forall(x => x.endsWith("Z"))
    }

    var steps: Int = 0
    var cur: Array[String] = guide.aNodes.toArray
    var stepArray: Array[Int] = Array.ofDim(cur.length)
    while (!finished(cur)) {
      guide.directions.foreach(d => {
        cur = cur.map(node => {
          val tuple = guide.map(node)
          if d == 'L' then tuple._1 else tuple._2
        })
        steps += 1
        cur.zipWithIndex.foreach((n, i) => {
          if n.endsWith("Z") && stepArray(i) == 0 then stepArray(i) = steps
        })
        if stepArray.forall(x => x > 0) then {
          println(stepArray.toSeq)
          return lcmOfArray(stepArray)
        }
      })
    }
    0
  }

  val filename = "input/p08.txt"

  try {
    val guide = parseFile()
   // println(guide)
  //  println(part1(guide))
    println(part2(guide))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
