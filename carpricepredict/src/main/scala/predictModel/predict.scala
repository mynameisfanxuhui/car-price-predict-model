package predictModel

// Each library has its significance, I have commented when it's used
import org.apache.log4j._
import org.apache.spark._
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.feature.VectorIndexer
import org.apache.spark.ml.regression.{GBTRegressor, RandomForestRegressor}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{IntegerType, StructField, StructType}

object predict extends Serializable{
  Logger.getLogger("org").setLevel(Level.ERROR)
  val conf = new SparkConf().setAppName("question4")
  conf.setMaster("local")
  val sc = new SparkContext(conf)
  val spark : SparkSession = SparkSession.builder().appName("Question4").config("spark.master", "local").getOrCreate()

  def main (args:Array[String]): Unit = {
    //val inputPath = args(0)
    val inputPath = "final_data2.csv"
    // Load and parse the data file, converting it to a DataFrame.
    //|price|abtest|vehicleType|gearbox|powerPS|model|kilometer|fuelType|brand|notRepairedDamage|
    val schema = StructType(
        StructField("price", IntegerType, nullable = true) ::
        StructField("abtest", IntegerType, nullable = true) ::
        StructField("vehicleType", IntegerType, nullable = true) ::
        StructField("gearbox", IntegerType, nullable = true) ::
        StructField("powerPS", IntegerType, nullable = true) ::
        StructField("model", IntegerType, nullable = true) ::
        StructField("kilometer", IntegerType, nullable = true) ::
        StructField("fuelType", IntegerType, nullable = true) ::
        StructField("brand", IntegerType, nullable = true) ::
        StructField("notRepairedDamage", IntegerType, nullable = true) ::
        Nil
    )
    val data = spark.read.format("libsvm").load("libsvmResult1.txt")
    //val data = spark.read.format("libsvm").load("text.txt")
    //data1.show(10)
    //data1.coalesce(1).write.csv("c1Output")
    //val data = spark.read.option("header", "true").schema(schema).csv(inputPath)
    data.show(10)

    // Automatically identify categorical features, and index them.
    // Set maxCategories so features with > 4 distinct values are treated as continuous.
    val featureIndexer = new VectorIndexer()
      .setInputCol("features")
      .setOutputCol("indexedFeatures")
      .setMaxCategories(4)
      .fit(data)

    // Split the data into training and test sets (30% held out for testing).
    val Array(trainingData, testData) = data.randomSplit(Array(0.7, 0.3))

    // Train a RandomForest model.
    val rf = new RandomForestRegressor()
      .setLabelCol("label")
      .setFeaturesCol("indexedFeatures")

    // Chain indexer and forest in a Pipeline.
    val pipeline1 = new Pipeline()
      .setStages(Array(featureIndexer, rf))
    // Train model. This also runs the indexer.
    val model1 = pipeline1.fit(trainingData)
    // Make predictions.
    val predictions1 = model1.transform(testData)

    val rmseEvaluator = new RegressionEvaluator()
      .setLabelCol("label")
      .setPredictionCol("prediction")
      .setMetricName("rmse")

    val maeEvaluator = new RegressionEvaluator()
      .setLabelCol("label")
      .setPredictionCol("prediction")
      .setMetricName("mae")

    val mseEvaluator = new RegressionEvaluator()
      .setLabelCol("label")
      .setPredictionCol("prediction")
      .setMetricName("mse")

    val rmse1 = rmseEvaluator.evaluate(predictions1)
    println("Random forest result: Root Mean Squared Error (RMSE) on test data = " + rmse1)
    val maeRT = maeEvaluator.evaluate(predictions1)
    println("Random forest result: MAE on test data = " + maeRT)
    val mseRT = mseEvaluator.evaluate(predictions1)
    println("Random forest result: MSE on test data = " + mseRT)


    // Train a GBT model.
    val gbt = new GBTRegressor()
      .setLabelCol("label")
      .setFeaturesCol("indexedFeatures")
      .setMaxIter(10)

    // Chain indexer and GBT in a Pipeline.
    val pipeline = new Pipeline()
      .setStages(Array(featureIndexer, gbt))

    // Train model. This also runs the indexer.
    val model = pipeline.fit(trainingData)

    // Make predictions.
    val predictions = model.transform(testData)

    // Select example rows to display.
    predictions.select("prediction", "label", "features").show(5)


    val rmse = rmseEvaluator.evaluate(predictions)
    println("Gradient Boost Regression result: Root Mean Squared Error (RMSE) on test data = " + rmse)
    val maeGRT = maeEvaluator.evaluate(predictions1)
    println("Gradient Boost Regression result: MAE on test data = " + maeGRT)
    val mseGRT = mseEvaluator.evaluate(predictions1)
    println("Gradient Boost Regression result: MSE on test data = " + mseGRT)

    sc.stop()
  }
}
