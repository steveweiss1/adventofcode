package adventofcode.y2023

import adventofcode.y2023.P04.Card
import adventofcode.y2023.P07.Hand.{Five, Four, FullHouse, Three, HighCard, Pair, TwoPair}

import java.lang.Character.isDigit
import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object P07 extends App {

  enum Hand(val value: Int) extends Ordered[Hand] {
    case Five extends Hand(100)
    case Four extends Hand(90)
    case FullHouse extends Hand(80)
    case Three extends Hand(70)
    case TwoPair extends Hand(60)
    case Pair extends Hand(50)
    case HighCard extends Hand(1)

    def compare(that: Hand): Int = value - that.value
  }

  def rankHand(h : String): Hand = {
    val freqs = h.groupBy(c => c).view.mapValues(_.length).toList.sortBy(-_._2)
    val first = freqs.head._2
    val rank: Hand = first match {
      case 5 => Five
      case 4 => Four
      case 3 => {
        val second = freqs(1)._2
        if second == 2 then FullHouse else Three
      }
      case 2 => {
        val second = freqs(1)._2
        if second == 2 then TwoPair else Pair
      }
      case 1 => HighCard
    }
    rank
  }

  def rankHand2(h: String): Hand = {
    if (!h.contains('J')) return rankHand(h)
    val chars = List('A','2','3','4','5','6','7','8','9','T','Q','K')
    chars.map(c => {
      rankHand(h.replace('J', c))
    }).maxBy(_.value)
  }

  case class Line(hand: String, bet: Int) extends Ordered [Line]{
    val rank: Int = rankHand2(hand).value
    def compare(other: Line): Int = {
      if (rank != other.rank) {
        return rank - other.rank
      }
      for (i <- 0 until hand.length) {
        if hand(i) != other.hand(i) then
          return value(hand(i)) - value(other.hand(i))
      }
      throw Exception("equal")
    }
  }

  def value(c: Char): Int = {
    c match {
      case 'A' => 20
      case 'K' => 19
      case 'Q' => 18
      case 'J' => 1
      case 'T' => 10
      case x => x - '0'
    }
  }

  def parseFile(): Seq[Line] = {
    Source.fromFile(filename).getLines().map {
      case s"$hand $bet" => Line(hand, bet.toInt)
    }
  }.toSeq


  def part1(lines: Seq[Line]): Int = {
    val sortedLines: Seq[Line] = lines.sortWith((l1, l2) => l1.compare(l2) < 0)
    val pairs: Seq[(Line, Int)] = sortedLines.zip(1 to sortedLines.length)
    pairs.map((l, i) => l.bet * i).sum
  }

  def part2(lines: Seq[Line]): Int = {
    val sortedLines: Seq[Line] = lines.sorted
    val pairs: Seq[(Line, Int)] = sortedLines.zip(1 to sortedLines.length)
    println(sortedLines)
    pairs.map((l, i) => l.bet * i).sum
  }

  val filename = "input/p07.txt"

  try {
    val lines = parseFile()
    println(part2(lines))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
