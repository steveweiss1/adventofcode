package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.annotation.tailrec
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break
object P16 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }


  def parseFile(): Array[Array[Char]] = {
    getLines.map(_.toCharArray).toArray
  }

  enum Direction:
    case UP, DOWN, LEFT, RIGHT

  def part1(grid: Array[Array[Char]]) : Int = {
    traverseGrid(grid, 0, -1, Direction.RIGHT)
  }

  private def traverseGrid(grid: Array[Array[Char]], row: Int, col: Int, direction: Direction) = {
    val seen: mutable.Set[(Int, Int, Direction)] = mutable.Set()
    dfs(row, col, grid, seen, direction)
    val map: Map[(Int, Int), mutable.Set[(Int, Int, Direction)]] = seen.groupBy((r, c, d) => (r, c))
   // println(map.keySet.toList.sorted.mkString(" "))
    map.size
  }

  def part2(grid: Array[Array[Char]]): Int = {
    val maxFromRow = grid.indices.map(r => traverseGrid(grid, r, -1, Direction.RIGHT).max(traverseGrid(grid, r, grid(0).length, Direction.LEFT))).max
    val maxFromCol = grid(0).indices.map(c => traverseGrid(grid, -1, c, Direction.DOWN).max(traverseGrid(grid, grid.length, c, Direction.UP))).max
    maxFromRow.max(maxFromCol)
  }

  def move(row: Int, col: Int, direction: Direction) : (Int, Int) = {
    var r = row
    var c = col
    direction match {
      case Direction.UP =>  r -= 1
      case Direction.DOWN => r += 1
      case Direction.LEFT =>  c -= 1
      case Direction.RIGHT =>  c += 1
    }
    (r, c)
  }
  def dfs(row: Int, col: Int, grid: Array[Array[Char]], seen: mutable.Set[(Int, Int, Direction)], direction: Direction) : Unit = {
    var (r, c) = move(row, col, direction)

    while (true) {
      //println(r + " " + c + " " + seen)
      if (r < 0 || r == grid.length || c < 0 || c == grid.length) return
      val newtuple = (r, c, direction)
      if (seen.contains(newtuple)) return
      seen.add(newtuple)
      grid(r)(c) match
        case EMPTY => {
          val rc = move(r, c, direction)
          r = rc._1
          c = rc._2
        }
        case DASH => {
          if (Set(Direction.LEFT, Direction.RIGHT).contains(direction)) {
            val rc = move(r, c, direction)
            r = rc._1
            c = rc._2
          }
          else {
            dfs(r, c, grid, seen, Direction.LEFT)
            dfs(r, c, grid, seen, Direction.RIGHT)
            return
          }
        }
        case PIPE => {
          if (Set(Direction.UP, Direction.DOWN).contains(direction)) {
            val rc = move(r, c, direction)
            r = rc._1
            c = rc._2
          }
          else {
            dfs(r, c, grid, seen, Direction.UP)
            dfs(r, c, grid, seen, Direction.DOWN)
            return
          }
        }
        case SLASH => {
          val nextDir = direction match
            case Direction.UP => Direction.RIGHT
            case Direction.DOWN => Direction.LEFT
            case Direction.LEFT => Direction.DOWN
            case Direction.RIGHT => Direction.UP
          dfs(r, c, grid, seen, nextDir)
          return
        }
        case BSLASH => {
          val nextDir = direction match
            case Direction.UP => Direction.LEFT
            case Direction.DOWN => Direction.RIGHT
            case Direction.LEFT => Direction.UP
            case Direction.RIGHT => Direction.DOWN
          dfs(r, c, grid, seen, nextDir)
          return
        }
    }
    throw new Exception("oops")
  }

  val EMPTY='.'
  val DASH='-'
  val PIPE='|'
  val SLASH='/'
  val BSLASH='\\'

  val filename = "input/p16.txt"
  try {
    val grid = parseFile()
     println(part1(grid))
    println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
