"""
Main cli or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    start_spark,
    end_spark,
)


def main():
    # extract data
    extract()

    # start spark session
    spark = start_spark("Birthsdata")
    # load data into dataframe
    df = load_data(spark)
    df.show(10)
    # example metrics
    df = load_data(spark)
    df.createOrReplaceTempView("Birthsdata")

    describe(df)
    # query
    query(
        spark,
        df,
        """SELECT year, 
        SUM(births) AS total_births FROM Birthsdata 
        GROUP BY year ORDER BY total_births DESC""",
        "year",
    )

    # end spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
