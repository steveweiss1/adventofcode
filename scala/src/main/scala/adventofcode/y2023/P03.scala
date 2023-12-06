package adventofcode.y2023

import java.lang.Character.isDigit
import scala.collection.mutable
import scala.io.Source

object P03 extends App {


  def parseFile(filePath: String): Array[Array[Char]] = {
    val source = Source.fromFile(filePath)

    try {
      // Read lines from the file and convert each line to a char array
      val lines = source.getLines().toArray
      val charArray = lines.map(_.toCharArray)

      // Convert the array of char arrays to a 2D char array
      charArray
    } finally {
      source.close()
    }
  }

  private def part1(array: Array[Array[Char]]): Int = {
    var total = 0
    val seen: mutable.Set[Int] = mutable.Set()
    for (row <- array.indices) {
      var value = 0
      var start = -1
      for (col <- array.head.indices) {
        if (Character.isDigit(array(row)(col))) {
          if (start == -1) {
            start = col
          }
          value = value*10 + (array(row)(col).toInt - '0')
        }
        if ((!Character.isDigit(array(row)(col)) || col == array.head.length-1) && start != -1) {
          val end = col - 1
          var symbol = false
          for (i <- start-1 to end+1) {
            if (isSymbol(array, row-1, i)) {
              symbol = true
            }
            if (isSymbol(array, row + 1, i)) {
              symbol = true
            }
          }
          if (isSymbol(array, row , start - 1)) {
            symbol = true
          }
          if (isSymbol(array, row, end + 1)) {
            symbol = true
          }
          if (symbol) {
            //if (!seen(value)) {
              total += value
              println(value + " " + total + " " + (Character.isDigit(array(row)(col)) && col == array.head.length-1 ))
           //   seen.add(value)
            //}
          } else {
            println("skipping " + value)
          }
          start = -1
          value=0
        }
      }
    }
    total
  }

  case class Point(row: Int, col: Int)

  private def part2(array: Array[Array[Char]]): Int = {
    val starMap: mutable.Map[Point, mutable.ListBuffer[Int]] = mutable.Map()
    for (row <- array.indices) {
      var value = 0
      var start = -1
      for (col <- array.head.indices) {
        if (Character.isDigit(array(row)(col))) {
          if (start == -1) {
            start = col
          }
          value = value * 10 + (array(row)(col).toInt - '0')
        }
        if ((!Character.isDigit(array(row)(col)) || col == array.head.length - 1) && start != -1) {
          val end = col - 1
          for (i <- start - 1 to end + 1) {
            if (isStar(array, row - 1, i)) {
              starMap.getOrElseUpdate(Point(row-1, i), mutable.ListBuffer()) += value
            }
            if (isStar(array, row + 1, i)) {
              starMap.getOrElseUpdate(Point(row+1,i), mutable.ListBuffer()) += value
            }
          }
          if (isStar(array, row, start - 1)) {
            starMap.getOrElseUpdate(Point(row,start-1), mutable.ListBuffer()) += value
          }
          if (isStar(array, row, end + 1)) {
            starMap.getOrElseUpdate(Point(row,end+1), mutable.ListBuffer()) += value
          }

          start = -1
          value = 0
        }
      }
    }
    var total = 0
    for ((point, values) <- starMap) {
      if (values.size == 2) {
        val list = values.toList
        println(s"point: $point list: ${list.head} ${list.last}")
        var product = list.head * list.last
        total += product
      }
    }

    total
  }
// dedupe: 331436
//  no dedupe: 552835
// with end: 556367
  private def isSymbol(array: Array[Array[Char]], r: Int, c: Int): Boolean = {
    try {
      val k = array(r)(c)
      !Character.isDigit(k) && k != '.'
    } catch {
      case e: Exception => false
    }
  }

  private def isStar(array: Array[Array[Char]], r: Int, c: Int): Boolean = {
    try {
      array(r)(c) == '*'
    } catch {
      case e: Exception => false
    }
  }

  val filename = "input/p3.txt" // Replace with the actual filename
  try {
    val array = parseFile(filename)
    println("part1: " + part2(array))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
