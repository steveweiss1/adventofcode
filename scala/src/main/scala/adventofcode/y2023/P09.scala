package adventofcode.y2023

import scala.::
import scala.collection.mutable
import scala.io.Source

object P09 extends App {


  def parseFile(): List[List[Int]] = {
    Source.fromFile(filename).getLines().map {
      _.split(" ").map(_.toInt).toList
    }.toList
  }

  def part1(inputs: List[List[Int]]) :Int = {
    inputs.map(computeNext).sum
  }

  def part2(inputs: List[List[Int]]): Int = {
    inputs.map(computePrev).sum
  }

  def computeNext(inputs: List[Int]) : Int = {
    println("input = " + inputs.mkString(", "))
    val stack : mutable.Stack[mutable.ListBuffer[Int]] = mutable.Stack.empty
    stack.push(mutable.ListBuffer.from(inputs))

    var sum = inputs.last
    while(!stack.head.forall(_ == 0)) {
      val list = stack.head
      val buf: mutable.ListBuffer[Int] = mutable.ListBuffer()
      for (i <- 0 until list.length-1) {
        buf.append(list(i+1) - list(i))
      }
      stack.push(buf)
      sum += buf.last
    }
    println(sum)
    sum

  }

  def computePrev(inputs: List[Int]): Int = {
    //println("input = " + inputs.mkString(", "))
    val stack: mutable.Stack[List[Int]] = mutable.Stack.empty
    stack.push(inputs)

    while (!stack.head.forall(_ == 0)) {
      val list = stack.head
      val buf: mutable.ListBuffer[Int] = mutable.ListBuffer()
      for (i <- 0 until list.length - 1) {
        buf.append(list(i + 1) - list(i))
      }
      stack.push(buf.toList)
    }

    var value = 0
    while (stack.nonEmpty) {
      val first = stack.pop.head
      value = first - value
    }
    //println(value)
    value

  }

  val filename = "input/p09.txt"

  try {
    val lists = parseFile()
   // println(part1(lists))
    println(part2(lists))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
