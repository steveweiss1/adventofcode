package adventofcode.y2023

import scala.::
import scala.collection.mutable
import scala.io.Source
import scala.util.control.Breaks.break

object P10 extends App {
  enum Pipe(val c: Char, val up: Boolean, val down: Boolean, val left: Boolean, val right: Boolean) {
    case UPDOWN extends Pipe('|', true, true, false, false)
    case LEFTRIGHT extends Pipe('-', false, false, true, true)
    case UPRIGHT extends Pipe('L', true, false, false, true)
    case UPLEFT extends Pipe('J', true, false, true, false)
    case DOWNLEFT extends Pipe('7', false, true, true, false)
    case DOWNRIGHT extends Pipe('F', false, true, false, true)
    case GROUND extends Pipe('.', false, false, false, false)
    case START extends Pipe('S', true, true, true, true)
    case OUT extends Pipe('O', false, false, false, false)
    case IN extends Pipe('I', false, false, false, false)
  }

  def fromChar(c: Char): Pipe = {
    Pipe.values.find(_.c == c).getOrElse(throw Exception(c.toString))
  }

  def parseFile(): (Array[Array[Pipe]], Point) = {
    var start: Point = Point(0,0)
    val ar = Source.fromFile(filename).getLines().zipWithIndex.map {
      (line, row) => {
        line.zipWithIndex.map((c, col) => {
          val pipe = fromChar(c)
          if pipe == Pipe.START then start = Point(row, col)
          pipe
        }).toArray
      }
    }
    (ar.toArray, start)
  }

  case class Point(row: Int, col: Int)
  def part1(grid: Array[Array[Pipe]], start: Point) : (Int, Array[Array[Int]]) = {
    var maxDist: Int = 0
    val distGrid: Array[Array[Int]] = Array.fill(grid.length, grid(0).length)(Int.MaxValue)
    var possibles: List[Point] = getPossibles(start, grid)
    val seen: mutable.Set[Point] = mutable.Set()
    val queue: mutable.Queue[Point] = mutable.Queue()
    var curDist = 1
    queue.addAll(possibles)
    queue.append(null)
    seen.add(start)
    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      if (cur == null) {
        println("null")
        curDist += 1
        if (queue.nonEmpty)
          queue.append(null)
      } else if (!seen.contains(cur)) {
        println(s"cur = ${cur.row} ${cur.col}")
        distGrid(cur.row)(cur.col) = Math.min(curDist, distGrid(cur.row)(cur.col))
        maxDist = Math.max(maxDist, curDist)
        possibles = getPossibles(cur, grid)
        queue.addAll(possibles)
        seen.add(cur)
      }
    }
    print2DArray(distGrid)
    (maxDist, distGrid)
  }

  def getPossibles(point: Point, array: Array[Array[Pipe]]) : List[Point] = {
    val possibles = mutable.ListBuffer[Point]()
    var pipe : Pipe = array(point.row)(point.col)
    if (point.row > 0 && pipe.up) {
      if (array(point.row-1)(point.col).down) possibles.append(Point(point.row-1,point.col))
    }
    if (point.row < array.length - 1 && pipe.down) {
      if (array(point.row + 1)(point.col).up) possibles.append(Point(point.row + 1, point.col))
    }
    if (point.col > 0 && pipe.left) {
      if (array(point.row)(point.col-1).right) possibles.append(Point(point.row, point.col-1))
    }
    if (point.col < array(0).length-1 && pipe.right) {
      if (array(point.row)(point.col + 1).left) possibles.append(Point(point.row, point.col + 1))
    }

    possibles.toList
  }

  def print2DArray(array: Array[Array[Pipe]]): Unit = {
    for (row <- array) {
      for (element <- row) {
        print(s"${element.c}\t")
      }
      println() // Move to the next line for the next row
    }
  }

  def print2DArray(array: Array[Array[Int]]): Unit = {
    for (row <- array) {
      for (element <- row) {
        var k = if element == Int.MaxValue then '.' else element
        print(s"$k\t")
      }
      println() // Move to the next line for the next row
    }
  }

  val OUT = -1

  def part2(grid: Array[Array[Pipe]], maxGrid: Array[Array[Int]]): Int = {
    var sum : Int = 0
    val verticals = Set(Pipe.UPDOWN, Pipe.DOWNLEFT, Pipe.DOWNRIGHT)
    for (row <- grid.indices) {
      var crosses = 0
      for (col <- grid(0).indices) {
        if (maxGrid(row)(col) == Int.MaxValue) {
          if crosses == 1 then {
            sum = sum + 1
            maxGrid(row)(col) = -1
          }
        } else if (verticals.contains(grid(row)(col))) {
          crosses = 1 - crosses
        }
      }
    }
   // print2DArray(maxGrid)
    sum
  }

  val filename = "input/p10.txt"

  try {
    val tuple = parseFile()
    //println(print2DArray(tuple._1))
    val tuple2 = part1(tuple._1, tuple._2)
    println
    println
    println(part2(tuple._1, tuple2._2))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
