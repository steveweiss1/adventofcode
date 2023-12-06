package adventofcode.y2023

import java.lang.Character.isDigit
import scala.io.Source

object P02 extends App {
  //12 red cubes, 13 green cubes, and 14 blue


  private def parseFile(filename: String): Int = {
    var total = 0
    Source.fromFile(filename).getLines().foreach { line =>
      //Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue
      var mins =  Map("red" -> 0, "green" -> 0, "blue" -> 0)
      var args: Array[String] = line.split(": ")
      var gameno: Int = args.head.split(' ').last.toInt
      var rounds = args.last.trim.split("; ")
      rounds.foreach(round => {
        var picks = round.split(", ")
        picks.foreach(pick => {
          var pair = pick.split(' ')
          var n = pair.head.toInt
          var color = pair.last
          mins = mins.updated(color, Math.max(mins(color), n))
        })
      })
      val power = mins("red") * mins("green") * mins("blue")
      total += power
    }
    total
  }

  val filename = "input/p2.txt" // Replace with the actual filename
  try {
    val i = parseFile(filename)
    println(i)
  } catch {
    case e: Exception => println(s"Error: $e")
  }
}
