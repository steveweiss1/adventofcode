package adventofcode.y2023

import adventofcode.y2023.P10.filename
import adventofcode.y2023.P25.Edge

import scala.::
import scala.collection.mutable
import scala.io.{BufferedSource, Source}
import scala.util.Random
import scala.util.control.Breaks.break

object P25 extends App {

  case class Edge(p1: String, p2: String)

  def edge(s: String, t: String) = {
    val sorted = Seq(s,t).sorted
    Edge(sorted.head, sorted.last)
  }
  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }
  def parseFile(): List[Edge] = {
    getLines.flatMap(line => {
      val nodes = line.split(' ')
      val first = nodes.head.substring(0, nodes.head.length-1)
      nodes.tail.flatMap(n => Seq(edge(first, n), edge(n, first)))
    }).toSet.toList
  }

  def toMap(edges: List[Edge]) : Map[String, List[Edge]] = {
    edges
      .flatMap(edge => List(edge.p1 -> edge, edge.p2 -> edge))
      .groupBy { case (string, _) => string }
      .view.mapValues(_.map { case (_, edge) => edge }).toMap
  }

  def part1(edges: List[Edge]): Unit = {
    val nodes: Vector[String] = edges.flatMap(e => Seq(e.p1, e.p2)).toSet.toVector
    val graph = toMap(edges)
    var seenEdges = mutable.ListBuffer[Edge]()
   /* (0 until 500).foreach(ignored => {
      val start = nodes(Random.nextInt(nodes.size))
      val end = nodes(Random.nextInt(nodes.size))
      if (!start.equals(end)) {
        //val seen = mutable.Set[Edge]()
        //val path = mutable.ListBuffer[Edge]()
        //dfs(graph, start, end, seen, path)
        val path = bfs(graph, start, end)
        if (path.size > 2)
          seenEdges.addAll(path)
      }
    })
   val mostSeenEdges = seenEdges.groupBy(e => e).view.mapValues(e => e.size).toList.sortBy(_._2).reverse.toList
   println(mostSeenEdges.slice(0, 6))*/

    val seen = mutable.Set[Edge]()
    val removed = List(edge("mlp", "qqq"), edge("vsx", "zbr"), edge("jxx", "qdp"))
    seen.addAll(removed)
    dfs(graph, "mlp", seen)
    removed.foreach(seen.remove)
    var seenNodes = seen.flatMap(e => List(e.p1, e.p2)).toSet.size
    println(seenNodes)

    seen.clear
    seen.addAll(removed)
    dfs(graph, "qqq", seen)
    removed.foreach(seen.remove)
    seenNodes = seen.flatMap(e => List(e.p1, e.p2)).toSet.size
    println(seenNodes)
  }

  case class State(node: String, path: List[Edge])
  def bfs(graph: Map[String, List[Edge]], start: String, end: String) : List[Edge] = {
    val queue = mutable.Queue[State]()
    queue.append(State(start, List()))
    while (queue.nonEmpty) {
      val state = queue.dequeue()
      Random.shuffle(graph(state.node)).foreach(edge => {
        if (state.path.isEmpty || state.path.last != edge) {
          val other = if edge.p1.equals(state.node) then edge.p2 else edge.p1
          val newState = State(other, state.path :+ edge)
          queue.append(newState)
          if (other.equals(end)) {
            return newState.path
          }
        }
      })
    }
    throw new Exception("oops")
  }

  def dfs(graph: Map[String, List[Edge]], cur: String, seen: mutable.Set[Edge]): Unit = {
    graph(cur).foreach(edge => {
      if (!seen.contains(edge)) {
        seen.add(edge)
        val other = if edge.p1.equals(cur) then edge.p2 else edge.p1
        dfs(graph, other, seen)
      }
    })
  }

  val filename = "input/p25.txt"
  try {
    val lines = parseFile()
    part1(lines)
    //println(part2(lines))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
