package adventofcode.y2023

import adventofcode.y2023.P10.filename

import scala.::
import scala.annotation.tailrec
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks.break

object P15 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }


  def parseFile(): Array[String] = {
    getLines.toList.head.split(',')
  }

  def part1(strings: Array[String]) : Int = {
    strings.map(hash).sum
  }

  case class Lens(label: String, value: Int)

  def part2(strings: Array[String]) : Int = {
    val array:Array[mutable.ListBuffer[Lens]] = Array.fill(256){mutable.ListBuffer()}
    strings.foreach { str =>
      println(str)
          str match {
            case s"$label=$n" =>
              val h = hash(label)
              val foundLens = array(h).zipWithIndex.find(_._1.label.equals(label))
              val newLens = Lens(label, n.toInt)
              if (foundLens.nonEmpty) {
                array(h)(foundLens.get._2) = newLens
              } else {
                array(h).append(newLens)
              }
            case s"$label-" =>
              val h = hash(label)
              val foundLens = array(h).zipWithIndex.find(_._1.label.equals(label))
              if (foundLens.nonEmpty) array(h).remove(foundLens.get._2)
          }
     // println(array.mkString(","))
    }

    array.zipWithIndex.map((lb, idx) => {
      lb.zipWithIndex.map((lens, listIndex) => (idx+1) * (listIndex+1) * lens.value).sum
    }).sum

  }

  def part2_immutable(strings: Array[String]): Int = {
    val theArray: Array[List[Lens]] = Array.fill(256) {
      List()
    }
    strings.foldLeft(theArray) { (array, str) =>
      println(str)
      str match {
        case s"$label=$n" =>
          val h = hash(label)
          val newLens = Lens(label, n.toInt)
          if (array(h).isEmpty) {
            array(h) = List(newLens)
          } else {
            val foundLens = array(h).zipWithIndex.find(_._1.label.equals(label))
            if (foundLens.nonEmpty) {
              val foundIdx = foundLens.get._2
              val (front, back)= array(h).splitAt(foundIdx)
              array(h) = (front :+ newLens) ++ back.tail
            } else {
              array(h) = array(h) :+ newLens
            }
          }
        case s"$label-" =>
          val h = hash(label)
          val foundLens = array(h).zipWithIndex.find(_._1.label.equals(label))
          if (foundLens.nonEmpty) {
            val foundIdx = foundLens.get._2
            val (front, back) = array(h).splitAt(foundIdx)
            array(h) = front ::: back.tail
          }
      }
      array
      // println(array.mkString(","))
    }

    theArray.zipWithIndex.map((lb, idx) => {
      lb.zipWithIndex.map((lens, listIndex) => (idx + 1) * (listIndex + 1) * lens.value).sum
    }).sum

  }

  def hash(str: String) : Int = {
    val h = str.foldLeft(0) {
      (acc, c) => {
        var k = acc + c
        k *= 17
        k % 256
      }
    }
    h
  }
  // 102247 is wrong

  val filename = "input/p15.txt"
  try {
    val strings = parseFile()
    println(hash("rn"))
    println(hash("cm"))
    println(hash("qp"))
   // println(part1(strings))
    println(part2_immutable(strings))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
