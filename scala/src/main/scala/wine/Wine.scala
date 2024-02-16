package wine

import scala.io.Source


object Wine extends App {

  private def getLines: Iterator[String] = {
    Source.fromFile(filename).getLines()
  }
  //1924,CA,Cab Sauv - Up to - $15.99,2022,Lodi,Bourbon Barrel Aged,Cabernet Sauvignon,$15.00,Silver
  case class Line(winery: String, state: String, category: String, vintage: String, loc: String, vineyard: String, varietal: String, price: Int, award: String)
  def parseFile(): List[Line] = {
    getLines.map { line =>
      val cols = line.split(',')
      val price = cols(7).stripPrefix("$").toDouble.toInt
      val award = if cols(8).contains("Sweepstakes") then "Sweepstakes" else cols(8)
      Line(cols(0),cols(1),cols(2),cols(3),cols(4),cols(5),cols(6),price, award)
    }.toList
  }

  val multiplier = Map("Sweepstakes" -> 60, "Best of Class" -> 55, "Double Gold" -> 45, "Gold" -> 30, "Silver" -> 5, "Bronze" -> 0)

  def process(lines: List[Line]) : String = {
    val byWinery: Map[String, List[Line]] = lines.filter(!_.award.equals("Bronze")).groupBy(_.winery)
    byWinery.view.mapValues { wineryLines =>
      wineryLines.map(wine => {
        Math.max((wine.price-30)*(wine.price-30),0) * multiplier(wine.award)
      }).sum
    }.toList.sortBy(_._2).reverse.take(40).map((winery,_) => {
     toString(winery, byWinery(winery))
    }).mkString("\n")
  }

  def toString(winery: String, lines: List[Line]) : String = {
    winery + "\n" + lines.sortBy(_.price).reverse.map(line => {
      s""",${line.varietal},$$${line.price},${line.award},${line.loc},${line.vintage}"""
    }).mkString("\n")
  }

  val filename = "input/wine-input.csv"
  try {
    val lines = parseFile()

    println(process(lines))
  } catch {
    case e: Exception => e.printStackTrace()
  }
}
