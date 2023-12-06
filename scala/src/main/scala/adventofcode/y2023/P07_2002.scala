package adventofcode.y2023

import java.lang.Character.isDigit
import scala.collection.mutable
import scala.collection.mutable.{ArrayBuffer, ListBuffer}
import scala.io.Source

object P07_2002 extends App {

  trait Entry

  case class File(name: String, size: Long) extends Entry

  class Directory(name: String) extends Entry {
    val directories :mutable.Map[String, Directory] = mutable.Map()
    val files :mutable.Map[String, File] = mutable.Map()
    def size: Long = {
      files.values.map(_.size).sum + directories.values.map(_.size).sum
    }
    def addFile(f: File): Unit = {
      files.put(f.name, f)
    }
  }

  def parseFile(filePath: String): Directory = {
    var root : Directory = Directory("")
    val d = Directory("/")
    root.directories.put("/", d)
    val stack : mutable.Stack[Directory] = mutable.Stack()
    stack.push(root)
    Source.fromFile(filename).getLines().foreach { line =>
      line match {
        case s"$$ cd $dirname" => {
          if (dirname.equals("..")) {
            stack.pop()
          } else {
            stack.push(stack.head.directories(dirname))
          }
        }

        case s"dir $name" =>
          stack.head.directories.put(name, Directory(name))

        case s"$number $name" if number.matches("\\d+") =>
          stack.head.addFile(File(name, number.toLong))

        case "$ ls" => "ignore"
      }
    }
    d
  }



  val filename = "input/2022-07.txt" // Replace with the actual filename
  try {
    val directory = parseFile(filename)

  } catch {
    case e: Exception => e.printStackTrace()
  }
}
