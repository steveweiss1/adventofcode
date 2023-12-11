package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break

object P11 extends App {

  case class Grid(rows: Array[Set[Int]], emptyRows: Set[Int], emptyCols: Set[Int])

  def parseFile(): Grid = {
    val cols = mutable.Set[Int]()
    val emptyRows = mutable.Set[Int]()
    var lineLength = 0
    var lines: Array[Set[Int]] = Source.fromFile(filename).getLines().zipWithIndex.map {
      (line, row) => {
        lineLength = line.length
        val g = """#""".r.unanchored.findAllMatchIn(line).map(m => m.start).toSet
        cols.addAll(g)
        if (g.isEmpty)
          emptyRows.add(row)
        g
      }
    }.toArray
    val emptyCols = (0 until lineLength).filter(x => !cols.contains(x)).toSet
    Grid(lines, emptyRows.toSet, emptyCols)
  }

  def parse2(): Grid = {
    val rawLines = Source.fromFile(filename).getLines().toList
    val allCols = rawLines.head.indices.toSet
    val (r, c, l) = rawLines.zipWithIndex.foldLeft((Set[Int](), allCols, List[Set[Int]]())) {
      case ((emptyRows, emptyCols, rows), (line, rowNo)) =>
        val cols = """#""".r.unanchored.findAllMatchIn(line).map(m => m.start).toSet
        val newEmptyCols = emptyCols.diff(cols)
        val newEmptyRows = if (cols.isEmpty) emptyRows + rowNo else emptyRows
        (newEmptyRows, newEmptyCols, rows :+ cols)
    }
    Grid(l.toArray, r, c)
  }

  def part1(grid: Grid, n: Int): Long = {
    val list: List[(Int, Int)] = grid.rows.zipWithIndex.flatMap((row, index) => row.map(x => (index, x)).toList).toList
    val combos = list.combinations(2).toList
    //println(combos)
    combos.map(l => {
      val p1 = l(0)
      val p2 = l(1)
      val minr = Math.min(p1._1, p2._1)
      val maxr = Math.max(p1._1, p2._1)
      val y : Long = (minr until maxr).map(r => if grid.emptyRows.contains(r) then n else 1).sum
      val minc = Math.min(p1._2, p2._2)
      val maxc = Math.max(p1._2, p2._2)
      val x : Long = (minc until maxc).map(c => if grid.emptyCols.contains(c) then n else 1).sum
      x + y
    }).sum
  }

  def part1_2(grid: Grid, n: Int): Long = {
    val list: List[(Int, Int)] = grid.rows.zipWithIndex.flatMap((row, index) => row.map(x => (index, x)).toList).toList
    val combos = list.combinations(2).toList
    combos.map {
      case List(p1: (Int, Int), p2: (Int, Int)) =>
        val (minr, maxr) = (p1._1.min(p2._1), p1._1.max(p2._1))
        val y: Long = (minr until maxr).map(r => if grid.emptyRows.contains(r) then n else 1).sum
        val minc = Math.min(p1._2, p2._2)
        val maxc = Math.max(p1._2, p2._2)
        val x: Long = (minc until maxc).map(c => if grid.emptyCols.contains(c) then n else 1).sum
        x + y
    }.sum
  }


  val filename = "input/p11-sample.txt"

  try {
    val grid = parse2()
    println(s"${grid.rows.mkString("Array(", ", ", ")")} ${grid.emptyRows} ${grid.emptyCols}")
    println("part1 = " + part1(grid, 2))
    println("part1 = " + part1_2(grid, 2))
    println("part2test = " + part1(grid, 100))
    println("part1test = " + part1_2(grid, 100))
    println("part2 final = " + part1(grid, 1000000))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
