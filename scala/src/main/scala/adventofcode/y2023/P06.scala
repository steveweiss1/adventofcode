package adventofcode.y2023

import java.lang.Character.isDigit
import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object P06 extends App {

  case class Trial1(time: Int, distance: Int)  {
    def ways : Int = {
      (0 to time).map(speed => {
          val runTime = time - speed
          speed * runTime
        })
        .count(dist => dist > distance)
    }
  }

  case class Trial2(time: Int, distance: Long) {
    def ways: Int = {
      (0 to time).map(speed => {
          val runTime = (time - speed).toLong
          speed * runTime
        })
        .count(dist => dist > distance)
    }
  }


 // Time:      71530
 // Distance:  940200

  try {
    // examples
    // examples
    val trials = Seq(Trial1(7, 9), Trial1(15, 40), Trial1(30, 200))

    /*Time:        40     92     97     90
    Distance:   215   1064   1505   1100*/
    val realTrials = Seq(Trial1(40, 125), Trial1(92, 1064), Trial1(97, 1505), Trial1(90, 1100))

    val product = realTrials.map(_.ways).product
    println(product)


    /*Time:        40     92     97     90
    Distance:   215   1064   1505   1100*/


    val example = Trial2(71530, 940200)
    println("ex = " + example.ways)
    val realTrial = Trial2(40929790, 215106415051100L)
    println(realTrial.ways)
   // val product = realTrials.map(_.ways).product
   // println(product)
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
