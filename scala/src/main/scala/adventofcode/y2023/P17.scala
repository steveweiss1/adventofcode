package adventofcode.y2023

import scala.collection.mutable
import scala.io.Source


object P17 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }


  def parseFile(): Array[Array[Int]] = {
    getLines.map { x => x.map(x => (x - '0')).toArray }.toArray
  }

  sealed trait Direction

  case object UP extends Direction

  case object DOWN extends Direction

  case object LEFT extends Direction

  case object RIGHT extends Direction

  def move(row: Int, col: Int, direction: Direction, steps: Int): (Int, Int) = {
    var r = row
    var c = col
    direction match {
      case UP => r -= steps
      case DOWN => r += steps
      case LEFT => c -= steps
      case RIGHT => c += steps
    }
    (r, c)
  }

  def adjacents(direction: Direction) : Array[Direction] = {
    if (direction == null) return Array(UP, DOWN, LEFT, RIGHT)
    if (Set(LEFT, RIGHT).contains(direction)) {
      return Array(UP, DOWN)
    }
    Array(LEFT, RIGHT)

  }
  def part1(grid: Array[Array[Int]]) : Int = {

    dijkstra(grid, 1, 3)
  }

  def part2(grid: Array[Array[Int]]): Int = {

    dijkstra(grid, 4, 10)
  }

  val MAXVAL = 1000000

  /*def dfs(grid: Array[Array[Int]], row: Int, col: Int, direction: Direction, seen: mutable.Set[(Int, Int)], cache: mutable.Map[(Int, Int, Direction), Int],
          timesInDirection: Int, stack: Int) : Int = {
    if (stack == 300) return MAXVAL
    if (row == grid.length-1 && col == grid(0).length-1)
      {
        return grid(row)(col)
      }
    if (timesInDirection > 2) return MAXVAL
    //println(row + " " + col + " " + direction + " " + timesInDirection)
    val tuple = move(row, col, direction)
    var r = tuple._1
    var c = tuple._2
    if (r < 0 || r == grid.length || c < 0 || c == grid.length) return MAXVAL
    if (seen.contains(r, c)) return MAXVAL
    if (cache.contains(r, c, direction)) return cache(r, c, direction)
    seen.add((r, c))
    val otherDirections = adjacents(direction)
    val d1 = dfs(grid, r, c, direction, seen, cache, timesInDirection + 1, stack+1)
    val d2 = dfs(grid, r, c, direction, seen, cache, timesInDirection + 2, stack+1)
    val d3 = dfs(grid, r, c, otherDirections(0), seen, cache, 0, stack+1)
    val d4 = dfs(grid, r, c, otherDirections(1), seen, cache, 0, stack+1)
    val minval = grid(r)(c) + (d1.min(d2).min(d3).min(d4))
    seen.remove((r,c))
    if (minval < MAXVAL)
      cache.put((r, c, direction), minval)
    minval
  }*/

  case class State(row: Int, col: Int, distance: Int, direction: Direction)

  val dirMap: Map[Direction, Int] = Map(LEFT -> 0, RIGHT -> 1, UP -> 2, DOWN -> 3)
  def dijkstra(grid: Array[Array[Int]], minSteps: Int, maxSteps: Int): Int = {
    val rows = grid.length
    val cols = grid(0).length

    val distances = Array.ofDim[Int](rows, cols, 4)
    for (i <- 0 until rows; j <- 0 until cols; k <- 0 until 4) distances(i)(j)(k) = Int.MaxValue

    val pq = mutable.PriorityQueue[State]()(Ordering.by(-_.distance))

    pq.enqueue(State(0, 0, 0, null))
    (0 until 4).foreach { k => distances(0)(0)(k) = grid(0)(0) }

    while (pq.nonEmpty) {
      val state = pq.dequeue()

      var directions = adjacents(state.direction)

      for (dir <- directions) {
        var gridDistances : Int = 0
        for (steps <- 1 to maxSteps) {
          val (newRow, newCol) = move(state.row, state.col, dir, steps)

          if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
            gridDistances += grid(newRow)(newCol)
            if (steps >= minSteps) {
              val newDist = state.distance + gridDistances
              val k = dirMap(dir)
              if (newDist < distances(newRow)(newCol)(k)) {
                distances(newRow)(newCol)(k) = newDist
                pq.enqueue(State(newRow, newCol, newDist, dir))
              }
            }
          }
        }
      }
    }

    distances(rows - 1)(cols - 1).indices.map(distances(rows - 1)(cols - 1)(_)).min
  }

  // 823 too low
  val filename = "input/p17.txt"
  try {
    val grid = parseFile()
   //println(part1(grid))
   println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
