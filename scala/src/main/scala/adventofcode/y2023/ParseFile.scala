package adventofcode.y2023

import scala.io.Source

object ParseFile extends App {
  private def parseFile(filename: String): List[List[Int]] = {
    Source.fromFile(filename).getLines().map { line =>
      line.split(" ").map(_.toInt).toList
    }.toList
  }

  val filename = "pairs.txt" // Replace with the actual filename
  try {
    val pairs = parseFile(filename)
    println("Parsed pairs:")
    pairs.foreach(p => println(p(0) + " " + p(1)))
  } catch {
    case e: Exception => println(s"Error: $e")
  }
}
