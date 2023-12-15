package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break

object P14 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }

  case class Grid(lines: Array[String])

  def parseFile(): Array[Array[Char]] = {
    getLines.map(l => l.toCharArray).toArray
  }

  val ROCK = 'O'
  val STOP = '#'
  val NONE = '.'
  def part1(grid: Array[Array[Char]]) : Int = {
    tiltUp(grid)

    computeWeight(grid)
  }

  private def computeWeight(grid: Array[Array[Char]]) = {
    grid.zip(grid.length to 1 by -1).map {
      (row, weight) =>
        row.count(_ == ROCK) * weight
    }.sum
  }

  def toString(g : Array[Array[Char]]) : String = {
    g.map(row => row.mkString).mkString
  }
  def part2(grid: Array[Array[Char]]): Int = {
    var g = cycle(grid)
    var foundLoop = false
    var start  = ""
    val s : mutable.Map[String, Int] = mutable.Map()
    var cont = true
    var i = 1
    while(cont) {
      g = cycle(g)
      var str = toString(g)
      if (s.contains(str)) {
        if (!foundLoop) {
          println("loop start = " + i)
          start = str
          foundLoop = true
        } else {
          println(i + " " + computeWeight(g))
          if (str.equals(start)) {
            println("loop end = " + i)
            cont = false
          }
        }
      } else {
        s.put(str, i)
      }
      i += 1
    }
    computeWeight(g)
  }

  private def cycle(grid: Array[Array[Char]]): Array[Array[Char]] = {
    var g = grid.map(identity)
    tiltUp(g)
    g = rotate(g)
    tiltUp(g)
    g = rotate(g)
    tiltUp(g)
    g = rotate(g)
    tiltUp(g)
    g = rotate(g)
    //print2DArray(g)
    g
  }

  def print2DArray(array: Array[Array[Char]]): Unit = {
    for (row <- array) {
      println(String(row))
    }
    println
  }
  
  def rotate(grid: Array[Array[Char]]) : Array[Array[Char]] = {
    grid.transpose.map(_.reverse)
  }
  private def tiltUp(grid: Array[Array[Char]]): Unit = {
    (1 until grid.length).foreach(rowIndex => {
      grid(0).indices.foreach(colIndex => {
        if (grid(rowIndex)(colIndex) == ROCK) {
          var i = 1
          while (rowIndex - i >= 0 && grid(rowIndex - i)(colIndex) == NONE) i += 1
          if (i > 1) {
            grid(rowIndex)(colIndex) = NONE
            grid(rowIndex - i + 1)(colIndex) = ROCK
          }
        }
      })
    })
  }

  val filename = "input/p14.txt"
  // 100178 - too low
  try {
    val grid = parseFile()
    val grid2 = grid.map(identity)
    println(part1(grid))
    println(part2(grid2))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
