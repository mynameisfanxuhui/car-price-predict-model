package predictModel

// Each library has its significance, I have commented when it's used
import org.apache.log4j._
import org.apache.spark._
import org.apache.spark.sql.SparkSession

object predict {
  Logger.getLogger("org").setLevel(Level.ERROR)
  val conf = new SparkConf().setAppName("question4")
  conf.setMaster("local")
  val sc = new SparkContext(conf)
  val spark : SparkSession = SparkSession.builder().appName("Question4").config("spark.master", "local").getOrCreate()

  def main (args:Array[String]): Unit = {
    //val inputPath = args(0)
    val inputPath = "final_data.csv"
    // Load and parse the data file, converting it to a DataFrame.
    val data = spark.read.csv(inputPath)
    data.show(100)

//    // Automatically identify categorical features, and index them.
//    // Set maxCategories so features with > 4 distinct values are treated as continuous.
//    val featureIndexer = new VectorIndexer()
//      .setInputCol("features")
//      .setOutputCol("indexedFeatures")
//      .setMaxCategories(4)
//      .fit(data)
//
//    // Split the data into training and test sets (30% held out for testing).
//    val Array(trainingData, testData) = data.randomSplit(Array(0.7, 0.3))
//
//    // Train a RandomForest model.
//    val rf = new RandomForestRegressor()
//      .setLabelCol("label")
//      .setFeaturesCol("indexedFeatures")
//
//    // Chain indexer and forest in a Pipeline.
//    val pipeline = new Pipeline()
//      .setStages(Array(featureIndexer, rf))
//
//    // Train model. This also runs the indexer.
//    val model = pipeline.fit(trainingData)
//
//    // Make predictions.
//    val predictions = model.transform(testData)
//
//    // Select example rows to display.
//    predictions.select("prediction", "label", "features").show(5)
//
//    // Select (prediction, true label) and compute test error.
//    val evaluator = new RegressionEvaluator()
//      .setLabelCol("label")
//      .setPredictionCol("prediction")
//      .setMetricName("rmse")
//    val rmse = evaluator.evaluate(predictions)
//    println(s"Root Mean Squared Error (RMSE) on test data = $rmse")
//
//    val rfModel = model.stages(1).asInstanceOf[RandomForestRegressionModel]
//    println(s"Learned regression forest model:\n ${rfModel.toDebugString}")


    sc.stop()
  }
}
