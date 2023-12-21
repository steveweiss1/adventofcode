package adventofcode.y2023


import scala.collection.mutable
import scala.io.Source


object P21 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }

  def parseFile(): Array[String] = {
    getLines.toArray
  }

  def part1(grid: Array[String]): Long = {
    val startRow = grid.zipWithIndex.filter(row => {
      row._1.contains("S")
    }).map(_._2).head
    val startCol = grid(startRow).indexOf('S')

    var set = Set((startRow, startCol))
    val directions = List((0,1), (0,-1), (-1,0), (1,0))

    (0 until 26501365).foreach {
      itr => {
        if (itr % 100 == 0) {
          println(itr)
          println(itr + " " + set.size + " " + set)
        }
        set = set.flatMap((r, c) => {
          directions.foldLeft(Set[(Int, Int)]()) {
            (acc, dir) => {
              val (mover, movec) = (r + dir._1, c + dir._2)
              var retval = acc

              val newr = if mover % grid.length >= 0 then mover % grid.length else grid.length + (mover % grid.length)
              val newc = if movec % grid(0).length >= 0 then movec % grid(0).length else grid(0).length + (movec % grid(0).length)

              //if (newr >= 0 && newr < grid.length && newc >= 0 && newc < grid(0).length) {
              if (grid(newr)(newc) != '#') {
                retval = acc + ((mover, movec))
              }
              //}
              retval
            }
          }
        })
      }
    }
    set.size
  }

  val filename = "input/p21-sample.txt"
  try {
    val lines = parseFile()
    println(part1(lines))
    //println(part2(workflows))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
