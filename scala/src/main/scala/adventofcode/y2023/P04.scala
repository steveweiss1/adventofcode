package adventofcode.y2023

import java.lang.Character.isDigit
import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object P04 extends App {

  case class Card(index: Int, winners: Seq[Int], mine: Seq[Int]) {
    val matches : Int = mine.intersect(winners).length
    val score : Int = if matches == 0 then 0 else math.pow(2, matches - 1).toInt
  }

  val ZERO = Card(0, Seq(), Seq())

  def parseFile(filePath: String): Seq[Card] = {
    Source.fromFile(filename).getLines().map { line =>
      def parseLine = {
        val Array(winnersS: String, mineS: String) = line.split('|')
        val first = winnersS.split("\\s+")
        val index = first(1).substring(0, first(1).length - 1).toInt
        val winners = first.slice(2, winnersS.length).map(s => s.toInt).toSeq
        val mine = mineS.trim.split("\\s+").map(s => s.toInt).toSeq
        Card(index, winners, mine)
      }
// Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
      def rParseLine = {
        val regex = """Card\s+(\d+):\s+([\d ]+)\|([\d ]+)""".r.unanchored
        val m = regex.findFirstMatchIn(line).get
        println(m.group(1) + " " + m.group(2))
      }

      def matchParseLine = {
        line match {
          case s"Card $index: $winning|$mine" => {
            var w = """\d+""".r.unanchored.findAllIn(winning).map(x => x.toInt).toList
            var m = """\d+""".r.unanchored.findAllIn(mine).map(x => x.toInt).toList
            Card(index.trim.toInt, w, m)
          }
          case _ => throw Exception("oops")
        }
      }

      

      //rParseLine
      matchParseLine
      parseLine
    }.toSeq
  }

  def part1(cards: Seq[Card]): Int = {
    cards.map(_.score)
      .sum
  }

  def part2Itr(cards: Seq[Card]): Int = {
    val cardsByIndex: Map[Int, Card] = cards.map(card => card.index -> card).toMap
    val ar: Array[Int] = Array.ofDim(cards.size + 1)

    cards.foreach(card => {
      ar(card.index) = ar(card.index) + 1
      for (i <- 1 to card.matches) {
        val j = card.index + i
        ar(j) = ar(j) + ar(card.index)
      }
    })

    ar.sum
  }

  def part2Fold(cards: Seq[Card]): Unit = {
    val cardsByIndex: Map[Int, Card] = cards.map(card => card.index -> card).toMap

    def cardsWon(card: Card): List[Int] =
      (card.index + 1 until card.index + 1 + card.matches)
        .filter(cardsByIndex.contains)
        .toList

    val cardMapping: Map[Int, List[Int]] = cards.foldLeft(Map.empty[Int, List[Int]]) {
      case (acc, card) =>
        acc + (card.index -> cardsWon(card))
    }
    println(cardMapping)
  }

  def part2(cards: Seq[Card]): Int = {
    val cardsByIndex: Map[Int, Card] = cards.map(card => card.index -> card).toMap
    def recScore(i: Int): Int = {
      val card = cardsByIndex.getOrElse(i, ZERO)
      if (card.index == 0) return 0
      var total = 1
      if (card.matches > 0) {
        for (j <- 1 to card.matches) {
            total += recScore(i + j)
        }
      }

      total
    }
    cards.map(card => recScore(card.index)).sum
  }

  val filename = "input/p04.txt" // Replace with the actual filename
  try {
    val cards = parseFile(filename)
    println(cards)
    println("part1: " + part1(cards))
    //println("part2: " + part2(cards))
    println("part2Fold: " + part2Fold(cards))

    /*part1: 24733
    part2: 5422730*/
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
