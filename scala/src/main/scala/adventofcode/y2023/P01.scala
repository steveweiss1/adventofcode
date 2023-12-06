package adventofcode.y2023

import java.lang.Character.isDigit
import scala.io.Source

object P01 extends App {
  private def replace(line: String): String = {
    var retval = ""
    var l = line
    while (l.nonEmpty) {
      if (l.startsWith("one")) {
        retval += "1"
      } else if (l.startsWith("two")) {
        retval += "2"
      } else if (l.startsWith("three")) {
        retval += "3"
      } else if (l.startsWith("four")) {
        retval += "4"
      } else if (l.startsWith("five")) {
        retval += "5"
      } else if (l.startsWith("six")) {
        retval += "6"
      } else if (l.startsWith("seven")) {
        retval += "7"
      } else if (l.startsWith("eight")) {
        retval += "8"
      } else if (l.startsWith("nine")) {
        retval += "9"
      } else {
        retval += l.head
      }
      l = l.tail
    }
    retval

  }

  private def parseFile(filename: String): Int = {
    var total = 0
    Source.fromFile(filename).getLines().foreach { line =>
      var n = 0
      var l = replace(line)
      l.toCharArray.foreach(c => {
        if (n == 0 && isDigit(c)) {
          var k = c.toInt - '0'
          n = 10 * k
        }
      })
      println(line + " " + l + " " + n)
      var found = false
      l.toCharArray.reverse.foreach(c => {
        if (!found && isDigit(c)) {
          var k = c.toInt - '0'
          n += k
          found = true
        }
      })
      total += n
      println(line + " " + l + " " + n)
    }
    total
  }

  val filename = "p1.txt" // Replace with the actual filename
  try {
    val i = parseFile(filename)
    println(i)
  } catch {
    case e: Exception => println(s"Error: $e")
  }
}
