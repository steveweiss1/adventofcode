package adventofcode.y2023

import adventofcode.y2023.P19.RangeSet

import scala.collection.mutable
import scala.io.Source


object P19 extends App {
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }

 val LT = '<'
 val GT = '>'

  trait Instruction {
    def nextState: String
  }

  case class Conditional(field: Char, comparator: Char, value: Int, nextState: String) extends Instruction
  case class NextState(nextState: String) extends Instruction
  case class Workflow(name: String, instructions: List[Instruction])

  case class Input(x: Int, m: Int, a: Int, s: Int)

  def parseFile(): (Map[String, Workflow], List[Input])  = {
    val wf  = mutable.Map[String, Workflow]()
    val inputs  = mutable.ListBuffer[Input]()
    getLines.foreach {
      case s"""{x=$x,m=$m,a=$a,s=$s}""" => inputs.append(Input(x.toInt, m.toInt, a.toInt, s.toInt))
      case s"""$name{$conditionals}""" =>
        val instructions: List[Instruction] = conditionals.split(',').map {
          case s"""$field<${v}:$nextState""" => Conditional(field(0), LT, v.toInt, nextState)
          case s"""$field>${v}:$nextState""" => Conditional(field(0), GT, v.toInt, nextState)
          case s"""${nextState}""" => NextState(nextState)
        }.toList
        wf += (name -> Workflow(name, instructions))
      case _ => println("ok")
    }
    (wf.toMap, inputs.toList)
  }

  def part1(workflows: Map[String, Workflow], inputs: List[Input]): Int = {
    inputs.filter(i => canAccept(i, workflows))
      .map(i => i.x + i.m + i.a + i.s)
      .sum
  }

  class MyRange extends Cloneable {
    var min:Int = 1
    var max:Int = 4000
    override def clone(): MyRange = {
      val r = super.clone().asInstanceOf[MyRange]
      r
    }

    override def toString: String = {
      s"""($min,$max)"""
    }

  }

  class RangeSet extends Cloneable {
    var x: MyRange = new MyRange
    var m: MyRange = new MyRange
    var a: MyRange = new MyRange
    var s: MyRange = new MyRange

    override def clone(): RangeSet = {
      val r = super.clone().asInstanceOf[RangeSet]
      r.x = x.clone
      r.m = m.clone
      r.a = a.clone
      r.s = s.clone
      r
    }
    override def toString: String = {
      s"$x $m $a $x"
    }
  }


  def part2(workflows: Map[String, Workflow]) : Long = {
    val rs = new RangeSet
    val wf = workflows("in")
    val ranges = dfs(workflows, wf, rs)

    val k: List[Long] = ranges.map( r =>
      (r.x.max.toLong - r.x.min.toLong + 1) * (r.m.max.toLong - r.m.min.toLong + 1) * (r.a.max.toLong - r.a.min.toLong + 1) * (r.s.max.toLong - r.s.min.toLong + 1)
      )
    k.sum
  }

  def dfs(workflows: Map[String, Workflow], cur: Workflow, theRangeSet: RangeSet): List[RangeSet] = {
    val result = mutable.ListBuffer[RangeSet]()
    var rangeSet = theRangeSet.clone
    var nextRangeSet = theRangeSet.clone
    cur.instructions.foreach {
      instruction =>
        instruction match
          case Conditional(field, op, value, ns) =>
            val (inputValue, nextInputValue) = field match
              case 'x' => (rangeSet.x, nextRangeSet.x)
              case 'm' => (rangeSet.m, nextRangeSet.m)
              case 'a' => (rangeSet.a, nextRangeSet.a)
              case 's' => (rangeSet.s, nextRangeSet.s)
            op match
              case LT => {
                inputValue.max = inputValue.max.min(value-1)
                nextInputValue.min = nextInputValue.min.max(value)
              }
              case GT => {
                inputValue.min = inputValue.min.max(value+1)
                nextInputValue.max = nextInputValue.max.min(value)
              }
            if (ns.equals("A")) {
              if (rangeSet.x.min == 1 && rangeSet.x.max == 4000) {
                println("ok")
              }
              result.append(rangeSet.clone)
            } else if (!ns.equals("R")) {
              result.addAll(dfs(workflows, workflows(ns), rangeSet.clone))
            }
          case NextState(ns) => {
            if (ns.equals("A")) {
              result.addAll(List(rangeSet.clone))
            } else if (!ns.equals("R")) {
              result.addAll(dfs(workflows, workflows(ns), rangeSet.clone))
            }
          }
          println(nextRangeSet)
          rangeSet = nextRangeSet
          nextRangeSet = rangeSet.clone
    }
    result.toList
  }

  // rkq{s<1860:A,s>2043:A,m>56:R,A}
  // {x=1416,m=956,a=1806,s=486}
  def canAccept(input: Input, workflows: Map[String, Workflow]) : Boolean = {
    var wf = workflows("in")
    var result = true
    var resultSet = false
    while (!resultSet) {
      var nextState: String = null
      wf.instructions.foreach {
        instruction =>
          if (nextState == null) {
            instruction match
              case Conditional(field, op, value, ns) =>
                val inputValue = field match
                  case 'x' => input.x
                  case 'm' => input.m
                  case 'a' => input.a
                  case 's' => input.s
                val isTrue = op match
                  case LT => inputValue < value
                  case GT => inputValue > value
                if (isTrue) nextState = ns
              case NextState(ns) => nextState = ns
          }
        }
        if (nextState.equals("A")) {
          result = true
          resultSet = true
        } else if (nextState.equals("R")) {
            result = false
            resultSet = true
        } else
          wf = workflows(nextState)
    }
    result
  }

  val filename = "input/p19.txt"
  try {
    val (workflows, inputs) = parseFile()
   // println(workflows)
   // println(inputs)
    //println(part1(workflows, inputs))
    println(part2(workflows))

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
