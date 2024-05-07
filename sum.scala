import org.apache.spark.sql.SparkSession

object SumOfNumbers {
  def main(args: Array[String]): Unit = {
    // Create a SparkSession
    val spark = SparkSession.builder().appName("SumOfNumbers").master("local[*]").getOrCreate()

    // Prompt the user to enter the first number
    println("Enter the first number:")
    val number1 = scala.io.StdIn.readInt()

    // Prompt the user to enter the second number
    println("Enter the second number:")
    val number2 = scala.io.StdIn.readInt()

    // Calculate the sum of numbers
    val sum = number1 + number2

    // Print the sum
    println(s"Sum of numbers: $sum")

    // Stop the SparkSession
    spark.stop()
  }
}

// scalac -classpath "C:\Users\Parth\Downloads\spark-3.5.1-bin-hadoop3\spark-3.5.1-bin-hadoop3/jars/*" HelloWorld.scala

// scala -classpath "C:\Users\Parth\Downloads\spark-3.5.1-bin-hadoop3\spark-3.5.1-bin-hadoop3/jars/*" SumOfNumbers 

// http://localhost:4040/