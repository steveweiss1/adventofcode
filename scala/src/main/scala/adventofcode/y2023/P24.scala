package adventofcode.y2023

import scala.collection.immutable.Set
import scala.collection.mutable
import scala.io.Source


object P24 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }
//19, 13, 30 @ -2,  1, -2

  case class Line(x: Long, y: Long, z: Long, dx: Int, dy: Int, dz: Int)  {
    def slope: Double = {
      dy.toDouble / dx.toDouble
    }
  }
  def parseFile(): Vector[Line] = {
    getLines.map {
      case s"""$x, $y, $z @ $dx, $dy, $dz""" => Line(x.trim.toLong,y.trim.toLong,z.trim.toLong,dx.trim.toInt,dy.trim.toInt,dz.trim.toInt)
    }.toVector
  }

  def part1(lines: Vector[Line]): Int  = {
    lines.combinations(2).map (x => willIntersect(x.head, x.last))
      .count(_ == true)
  }


  def willIntersect(l1: Line, l2: Line) : Boolean = {
    val (ix, iy) = findIntersection(l1.slope, l1.x, l1.y, l2.slope, l2.x, l2.y)
    if (ix < MIN || ix > MAX) return false
    if (iy < MIN || iy > MAX) return false

    if (((ix - l1.x) / l1.dx) < 0) return false
    if (((ix - l2.x) / l2.dx) < 0) return false

    if (((iy - l1.y) / l1.dy) < 0) return false
    if (((iy - l2.y) / l2.dy) < 0) return false
    true
  }

  def findIntersection(m1: Double, x1: Long, y1: Long, m2: Double, x2: Long, y2: Long): (Double, Double) = {
    // Solve for x
    val xIntersection = (y1 - y2 + m2 * x2 - m1 * x1) / (m2 - m1)

    // Substitute x into either line equation to find y
    val yIntersection = y1 + m1 * (xIntersection - x1)

    (xIntersection, yIntersection)
  }

  val filename = "input/p24.txt"
  /*val MIN = 7
  val MAX = 27*/

  val MIN = 200000000000000L
  val MAX = 400000000000000L

  try {
    val lines = parseFile()
    println(part1(lines))
    //println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
