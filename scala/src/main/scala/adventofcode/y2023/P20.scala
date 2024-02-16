package adventofcode.y2023

import adventofcode.y2023.P10.filename
import adventofcode.y2023.P25.Edge

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}

object P20 extends App {

  val HIGH = 1
  val LOW = 0
  val NOTHING = -1

  val BROAD = 0
  val FLIP = 1
  val CONJUNCTION = 2

  val BROADCASTER_NAME = "broadcaster"

  case class Node(name: String, nodeType: Int, outputs: List[String])

  trait Module {
    def process(input: String, pulse: Int) : Int
  }

  class FlipFlip extends Module {
    var isOn : Boolean = false
    def process(input: String, pulse: Int) : Int = {
      if (pulse == LOW) {
        if (!isOn) {
          isOn = true
          HIGH
        } else {
          isOn = false
          LOW
        }
      } else {
        NOTHING
      }
    }
  }

  class Conjunction extends Module {

    val inputStates: mutable.Map[String, Int] = mutable.Map()

    def init(inputs: Set[String]): Unit = {
      inputs.foreach(i => inputStates.put(i, LOW))
    }

    def process(input: String, pulse: Int): Int = {
      inputStates.put(input, pulse)
      val hasLow = inputStates.exists(_._2 == LOW)
      if hasLow then HIGH else LOW
    }
  }

  class Broadcaster extends Module {
    def process(input: String, pulse: Int): Int = {
      pulse
    }
  }

  class Output extends Module {
    def process(input: String, pulse: Int): Int = {
      println("output got " + pulse)
      NOTHING
    }
  }

  class RX extends Module {
    var times = 0L
    def process(input: String, pulse: Int): Int = {
      times += 1
      if pulse == LOW then throw Exception("got low " + times)
      NOTHING
    }
  }

  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }
  def parseFile(): List[Node] = {
    getLines.map {
      case s"""$name -> $others""" =>
        val outputs = others.trim.split(',').map(_.trim).toList
        val prefix = name.charAt(0)
        val nodeType = if name.equals(BROADCASTER_NAME) then BROAD else if prefix == '%' then FLIP else CONJUNCTION
        val theName = if nodeType == BROAD then BROADCASTER_NAME else name.substring(1)
        Node(theName, nodeType, outputs)
    }.toList
  }

  def part1(nodes: List[Node]) : Unit = {
    val nodesByName = nodes.map(node => node.name -> node).toMap
    val nodesToPrefix: Map[String, List[String]] = nodes.flatMap(n => n.outputs.map(out => (out, n.name))).groupBy(x => x._1)
      .view.mapValues(_.map { case (_, p) => p }).toMap
    val modulesByName: Map[String, Module] = nodesByName.map(nodeEntry => {
      val module = nodeEntry._2.nodeType match
        case BROAD => Broadcaster()
        case FLIP => FlipFlip()
        case CONJUNCTION =>
          val c = Conjunction()
          c.init(nodesToPrefix(nodeEntry._1).toSet)
          c
      nodeEntry._1 -> module
    }) ++ Map("output" -> Output()) ++ Map("rx" -> RX())

    while(true) {
      push(LOW, nodesByName, modulesByName)
    }
    //val tuple = (0 until 1000000).map(ignored => push(LOW, nodesByName, modulesByName)).reduce((x, y) => (x._1 + y._1, x._2 + y._2))
    //tuple._1 * tuple._2
  }

  case class Payload(pulse: Int, name: String, inputName: String)
  def push(pulse: Int, nodesByName: Map[String, Node], modulesByName: Map[String, Module]) : (Int, Int) = {
    val queue : mutable.Queue[Payload] = mutable.Queue()
    queue.append(Payload(pulse, BROADCASTER_NAME, null))

    var lows = 0
    var highs = 0

    while (queue.nonEmpty) {
      val payload = queue.dequeue
      //println(" dequeue payload " + payload)
      if payload.pulse == LOW then lows+=1 else highs+=1
      val newPulse = modulesByName.get(payload.name).map(m => m.process(payload.inputName, payload.pulse)).orElse(Option(NOTHING)).get
      if (newPulse != NOTHING) {
        nodesByName(payload.name).outputs.foreach(output => queue.append(Payload(newPulse, output, payload.name)))
      }
    }
    //println((lows, highs))
    (lows, highs)
  }

  val filename = "input/p20.txt"
  try {
    val lines = parseFile()
    part1(lines)
    //println(part2(lines))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
