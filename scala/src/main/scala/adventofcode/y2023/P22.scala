package adventofcode.y2023

import scala.collection.mutable
import scala.io.Source


object P22 extends App {
//1,1,8~1,1,9
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }

  case class Point(x: Int, y: Int, z: Int)
  case class Brick(p1: Point, p2: Point)

  def parseFile(): Array[Brick] = {
    var mx=0
    var my=0
    var mz=0
    var r = getLines.map {
      case s"$a,$b,$c~$d,$e,$f" => {
        val br: Brick = Brick(Point(a.toInt, b.toInt, c.toInt), Point(d.toInt, e.toInt, f.toInt))
        mx = mx.max(br.p1.x).max(br.p2.x)
        my = my.max(br.p1.y).max(br.p2.y)
        mz = mz.max(br.p1.z).max(br.p2.z)
        br
      }
    }.toArray
    println(s"$mx $my $mz")
    r
  }

  val MAX_X = 9
  val MAX_Y = 9
  val MAX_Z = 334

  def rectanglesIntersect(brick1: Brick, brick2: Brick): Boolean = {
    // Check if one rectangle is to the left of the other
    val isToLeft = brick1.p2.x < brick2.p1.x || brick2.p2.x < brick1.p1.x

    // Check if one rectangle is to the right of the other
    val isToRight = brick1.p1.x > brick2.p2.x || brick2.p1.x > brick1.p2.x

    // Check if one rectangle is above the other
    val isAbove = brick1.p2.y < brick2.p1.y || brick2.p2.y < brick1.p1.y

    // Check if one rectangle is below the other
    val isBelow = brick1.p1.y > brick2.p2.y || brick2.p1.y > brick1.p2.y

    // If none of the above conditions are met, rectangles intersect
    !(isToLeft || isToRight || isAbove || isBelow)
  }
  def clear(brick: Brick, brickSet: mutable.Set[Brick]) : Boolean = {
    !brickSet.exists(other => {
        rectanglesIntersect(brick, other)
    })
  }
  def part1(bricks: Array[Brick]) : Int = {
    val brickStack: Array[mutable.Set[Brick]] = Array.fill(MAX_Z + 1) { mutable.Set() }
    bricks.foreach(brick => {
      (brick.p1.z to brick.p2.z).foreach(z => {
        brickStack(z).add(brick)
      })
    })
    // 1) drop them
    drop(brickStack, 2)

    // 2) Try to disintegrate
    val can : mutable.Set[Brick] = mutable.Set()
    val cant : mutable.Set[Brick] = mutable.Set()

    (175 to 1 by -1).foreach(z => {
      if (brickStack(z+1).isEmpty) {
        can.addAll(brickStack(z))
      } else {
        brickStack(z).foreach(lowerBrick => {
          val bricksWithout = brickStack(z).toSet - lowerBrick
          if (brickStack(z+1).forall(brick => bricksWithout.exists(b => rectanglesIntersect(brick, b)))) {
            can.add(lowerBrick)
          }
        })

        /*val brickMap = mutable.Map[Brick, Set[Brick]]()
        val nointersections = mutable.Set[Brick]()
        nointersections.addAll(brickStack(z-1))
        brickStack(z).foreach(brick => {
          brickStack(z - 1).foreach(lowerBrick => {
            if (rectanglesIntersect(lowerBrick, brick)) {
              nointersections.remove(lowerBrick)
              brickMap.put(lowerBrick, brickMap.getOrElse(lowerBrick, Set()) + brick)
            }
          })
        })
        can.addAll(nointersections)
        brickMap.foreach((b, set) => {
          if (set.size == 1) {
            cant.addAll(set)
          }
        })

        brickMap.foreach((b, set) => {
          can.addAll(set.filter(!cant.contains(_)))
        })*/
      }
    })
    can.size
  }

  def copy(ar: Array[mutable.Set[Brick]]): Array[mutable.Set[Brick]] = {
    ar.map(s => s.clone)
  }
  def part2(bricks: Array[Brick]): Int = {
    val brickStack: Array[mutable.Set[Brick]] = Array.fill(MAX_Z + 1) {
      mutable.Set()
    }
    bricks.foreach(brick => {
      (brick.p1.z to brick.p2.z).foreach(z => {
        brickStack(z).add(brick)
      })
    })
    // 1) drop them
    drop(brickStack, 2)

    // 2) Try to disintegrate
    var totalDrops = 0
    (175 to 1 by -1).foreach(z => {
        brickStack(z).filter(b => b.p2.z == z).foreach(lowerBrick => {
          val stackCopy = copy(brickStack)
          stackCopy(z).remove(lowerBrick)
          totalDrops += drop(stackCopy, z)
        })
    })
    totalDrops
  }

  private def drop(brickStack: Array[mutable.Set[Brick]], from: Int): Int = {
    var falls = 0
    (from to MAX_Z).foreach(curz => {
      brickStack(curz).foreach(brick => {
        var prevz = curz
        var cont = true
        while (cont && prevz > 1) {
          if (clear(brick, brickStack(prevz - 1))) {
            prevz -= 1
          } else {
            cont = false
          }
        }
        if (prevz < curz) {
          falls += 1
          val newBrick = Brick(Point(brick.p1.x, brick.p1.y, prevz), Point(brick.p2.x, brick.p2.y, brick.p2.z - (curz - prevz)))
          (brick.p1.z to brick.p2.z).foreach(z => {
            brickStack(z).remove(brick)
          })
          (newBrick.p1.z to newBrick.p2.z).foreach(z => {
            brickStack(z).add(newBrick)
          })
        }
      })
    })
    falls
  }

  val filename = "input/p22.txt"
  try {
    val grid = parseFile()
    //println(grid)
    //println(part1(grid))
    println(part2(grid))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
