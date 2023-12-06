package adventofcode.y2023

import scala.collection.immutable.NumericRange
import scala.collection.mutable
import scala.collection.mutable.ListBuffer
import scala.io.Source

object P05 extends App {

/*seed-to-soil map:
50 98 2
52 50 48*/

  def getDestinations(sources: List[Long], lines: Iterator[String]): List[Long] = {
    var l = lines.next()
    var line = lines.next()
    var dests : mutable.ListBuffer[Long] = mutable.ListBuffer()
    var used : mutable.Set[Long] = mutable.Set()
    while (line.nonEmpty) {
      val m = """(\d+) (\d+) (\d+)""".r.findFirstMatchIn(line).get
      var destStart = m.group(1).toLong
      var sourceStart = m.group(2).toLong
      var rangeSize = m.group(3).toLong

      for (src <- sources) {
        var range = sourceStart until sourceStart+rangeSize
        if (!used.contains(src) && range.contains(src)) {
          used.add(src)
          dests.append(src - (sourceStart - destStart))
        }
      }
      if (lines.hasNext)
        line = lines.next()
      else
        line=""
    }
    val rest: Seq[Long] = sources.diff(used.toList)
    dests.addAll(rest)

    dests.toList
  }

  case class Trip(dest: Long, sources: (Long, Long))

  def parseNext(lines: Iterator[String]): List[Trip] = {
    var l = lines.next()
    var line = lines.next()
    val out: mutable.ListBuffer[Trip] = mutable.ListBuffer()
    while (line.nonEmpty) {
      val m = """(\d+) (\d+) (\d+)""".r.findFirstMatchIn(line).get
      out.append(Trip(m.group(1).toLong, (m.group(2).toLong,m.group(2).toLong + m.group(3).toLong - 1)))
      if (lines.hasNext)
        line = lines.next()
      else
        line = ""
    }
    out.toList
  }

  def getIntersection(pair1: (Long, Long), pair2: (Long, Long)): Option[(Long, Long)] = {
    val start = Math.max(pair1._1, pair2._1)
    val end = Math.min(pair1._2, pair2._2)

    if (start <= end) Some((start, end)) else None
  }

  def getNonIntersectionRanges(pair1: (Long, Long), pair2: (Long, Long)): Seq[(Long, Long)] = {
    val intersectionStart = Math.max(pair1._1, pair2._1)
    val intersectionEnd = Math.min(pair1._2, pair2._2)

    val nonIntersectionBefore = if (pair1._1 < intersectionStart) Some((pair1._1, intersectionStart - 1)) else None
    val nonIntersectionAfter = if (pair1._2 > intersectionEnd) Some((intersectionEnd + 1, pair1._2)) else None

    val buffer = ListBuffer[(Long, Long)]()
    if (nonIntersectionBefore.nonEmpty) {
      buffer.append(nonIntersectionBefore.get)
    }
    if (nonIntersectionAfter.nonEmpty) {
      buffer.append(nonIntersectionAfter.get)
    }
    buffer.toList
  }

  

  def getDestinations2(sources: List[(Long, Long)], lines: Iterator[String]): List[(Long, Long)] = {
    val dests: mutable.ListBuffer[(Long, Long)] = mutable.ListBuffer()
    val trips = parseNext(lines);
    var unusedSources = sources
    trips.foreach { trip =>
      val nextSources = mutable.ListBuffer[(Long, Long)]()
      unusedSources.foreach { src =>
        val intersection = getIntersection(src, trip.sources)
        if (intersection.nonEmpty) {
          val destStart = trip.dest + (intersection.get._1 - trip.sources._1)
          val range = intersection.get._2 - intersection.get._1 - 1
          val value = (destStart, destStart + range)
          dests.append(value)
          val nonIntersections = getNonIntersectionRanges(src, trip.sources)
          nextSources.appendAll(nonIntersections)
        } else {
          nextSources.append(src)
        }
      }
      unusedSources = nextSources.toList
    }
    dests.addAll(unusedSources)
    dests.toList
  }

  def getDestinations3(sources: List[(Long, Long)], lines: Iterator[String]): List[(Long, Long)] = {
    val trips = parseNext(lines)

    val dests: (List[(Long, Long)], List[(Long, Long)]) = trips.foldLeft((List[(Long, Long)](), sources)) { case ((acc, unusedSources), trip) =>
      val (nextDests, nextUnusedSources) = unusedSources.foldLeft((List[(Long, Long)](), List[(Long, Long)]())) { case ((d, n), src) =>
        val intersection = getIntersection(src, trip.sources)
        if (intersection.nonEmpty) {
          val destStart = trip.dest + (intersection.get._1 - trip.sources._1)
          val range = intersection.get._2 - intersection.get._1 - 1
          val value = (destStart, destStart + range)
          (value :: d, getNonIntersectionRanges(src, trip.sources).toList ::: n)
        } else {
          (d, src :: n)
        }
      }
      (acc ::: nextDests, nextUnusedSources)
    }

    dests._1 ::: dests._2
  }

  def parseFile: List[Long] = {
    val theLines: Iterator[String] = Source.fromFile(filename).getLines()
    val firstLine = theLines.next()
    var seeds: List[Long] = firstLine match
      case s"seeds: $nums" => """\d+""".r.unanchored.findAllIn(nums).map(x => x.toLong).toList

    theLines.next()
    for (i <- 0 until 7) {
      seeds = getDestinations(seeds, theLines)
    }
    seeds
  }

  def parseFile2: List[Long] = {
    val theLines: Iterator[String] = Source.fromFile(filename).getLines()
    val firstLine = theLines.next()
    val seeds: List[Long] = firstLine match
      case s"seeds: $nums" => """\d+""".r.unanchored.findAllIn(nums).map(x => x.toLong).toList
    var listOfPairs: List[(Long, Long)] = seeds.grouped(2).map { case List(a, b) => (a, a+b-1) }.toList

    theLines.next()
    for (i <- 0 until 7) {
      listOfPairs = getDestinations3(listOfPairs, theLines)
    }
    listOfPairs.map(_._1)
  }

  def parseFileSampling: List[Long] = {
    val theLines: Iterator[String] = Source.fromFile(filename).getLines()
    val firstLine = theLines.next()
    val seeds: List[Long] = firstLine match
      case s"seeds: $nums" => """\d+""".r.unanchored.findAllIn(nums).map(x => x.toLong).toList
    var listOfPairs: List[List[Long]] = seeds.grouped(2).toList

    var samples: List[Long] = listOfPairs.flatMap(pair => {
      (pair.head until pair.head + pair.last by (pair.last / 500000)).toList
    })

    theLines.next()
    for (i <- 0 until 7) {
      println("iter " + i)
      samples = getDestinations(samples, theLines)
    }
    samples
  }

  val filename = "input/p05.txt" // Replace with the actual filename
  try {
    var results = parseFileSampling
    println(results.min)
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
