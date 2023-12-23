package adventofcode.y2023

import scala.collection.immutable.Set
import scala.collection.mutable
import scala.io.Source


object P23 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }


  def parseFile(): Array[Array[Char]] = {
    getLines.map(_.toArray).toArray
  }

  val START_COL = 1

  def part1(grid: Array[Array[Char]]) : Int = {
    var row=0
    var col=1
    dfs(grid, row, col)
  }

  def dfs(grid: Array[Array[Char]], r: Int, c: Int) : Int = {
    var (row, col) = (r, c)
    var len = 1
    while (row < grid.length - 1) {
      grid(row)(col) = 'x'
      val next = findNext(grid, row, col)
      if (next.isEmpty) return -100000
      if (next.size == 1) {
        val (nrow, ncol) = next.head
        row = nrow
        col = ncol
        len += 1
      } else {
        val mx = next.map((nrow, ncol) => {
          dfs(grid.map(_.clone), nrow, ncol)
        }).max + len
        return mx
      }
    }
    len-1
  }

  val PATH = Set('.', '<', '>', 'v', '^')
  def findNext(grid: Array[Array[Char]], r: Int, c: Int): Set[(Int, Int)] = {
    var set = Set[(Int,Int)]()
    if (r > 0 && PATH.contains(grid(r-1)(c))) {
      set += (r-1, c)
    }
    if (r < grid.length-1 && PATH.contains(grid(r + 1)(c))) {
      set += (r + 1, c)
    }
    if (c > 0 && PATH.contains(grid(r)(c - 1))) {
      set += (r, c - 1)
    }
    if (c < grid(0).length-1 && PATH.contains(grid(r)(c + 1))) {
      set += (r, c + 1)
    }
    set
  }

  def print2DArray(array: Array[Array[Char]]): Unit = {
    for (row <- array) {
      println(String(row))
    }
    println
  }

  // 5134 too low
  val filename = "input/p23.txt"
  try {
    val grid = parseFile()
    println(part1(grid))
    //println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
