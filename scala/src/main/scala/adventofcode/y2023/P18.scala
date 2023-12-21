package adventofcode.y2023

import scala.collection.mutable
import scala.io.Source


object P18 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }


  case class Line(direction: Char, length: Int, color: String)
  def parseFile(): Array[Line] = {
    getLines.map {
      case s"$direction $length (#$color)" => Line(direction.head, length.toInt, color)
    }.toArray
  }


  val IN = 0
  val EDGE = 1
  val OUT = 2

  def print2DArray(array: Array[Array[Int]]): Unit = {
    for (row <- array) {
      println(String(row.map(i => if i == 0 then '.' else if i == 1 then '-' else ' ')))
    }
    println
  }

  def part1(lines: Array[Line]) : Int = {
    var grid: Array[Array[Int]] = Array.ofDim(260, 640)
    var row = 155
    var col = 200
    grid(row)(col) = EDGE
    var (minRow, minCol, maxRow, maxCol) = (5000, 5000, 0, 0)

    lines.foreach(line => {
      val (rowDir, colDir) =  line.direction match {
        case 'U' => (-1, 0)
        case 'D' => (1, 0)
        case 'L' => (0, -1)
        case 'R' => (0, 1)
      }
      var newrow=0
      var newcol=0
      (1 to line.length).foreach(l => {
        val tuple = (row + l*rowDir, col + l*colDir)
        newrow = tuple._1
        newcol = tuple._2
        grid(newrow)(newcol) = EDGE
        minRow = minRow.min(newrow)
        maxRow = maxRow.max(newrow)
        minCol = minCol.min(newcol)
        maxCol = maxCol.max(newcol)
      })
      row = newrow
      col = newcol
    })
    setOuts(grid)

    grid = grid.transpose
    setOuts(grid)

    grid = grid.transpose

    (0 until 300).foreach(i => {
      findOuts(grid)
      grid = grid.transpose
      findOuts(grid)
      grid = grid.transpose
    })
//    print2DArray(grid)

    grid.map(r => {
      r.count(Set(EDGE, IN).contains(_))
    }).sum
  }

 /* def part2(grid: Array[Array[Int]]): Int = {

  }*/


  private def findOuts(grid: Array[Array[Int]]): Unit = {
    var set = true
    while (set) {
      set = false
      grid.foreach(r => {
        (1 until r.length).foreach(i => {
          if (r(i) == IN && (r(i-1) == OUT || r(i+1) == OUT)) {
            r(i) = OUT
            set = true
          }
        })
      })
    }
  }
  private def setOuts(grid: Array[Array[Int]]): Unit = {
    grid.foreach(r => {
      var i = 0
      while (i < r.length && r(i) == IN) {
        r(i) = OUT
        i += 1
      }
      i = r.indices.last
      while (i >= 0 && r(i) == IN) {
        r(i) = OUT
        i -= 1
      }
    })
  }
// 73111 - wrong
// 55141 - too high

  val filename = "input/p18.txt"
  try {
    val grid = parseFile()
    println(part1(grid))
    //println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
