package adventofcode.y2023

import scala.collection.mutable
import scala.io.Source

object P05_2002 extends App {

/*
[D]
[N] [C]
[Z] [M] [P]
012345678
1   2   3*/

  def parseFile: Array[mutable.Stack[Char]] = {
    val stacks :Array[mutable.Stack[Char]] = Array.fill(3)(mutable.Stack[Char]())
    Source.fromFile(filename).getLines().foreach { line =>
      val r = """\[([A-Z])]""".r.unanchored
      r.findAllMatchIn(line).foreach(m => {
        stacks(m.start / 3).append(m.group(1).charAt(0))
      })
    }
    stacks
  }


  val filename = "input/2022-05-sample.txt" // Replace with the actual filename
  try {
    parseFile

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
