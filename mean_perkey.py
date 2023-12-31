import apache_beam as beam

with beam.Pipeline() as p:
    '''
    Mean transform can be used to compute arithmetic mean of elements in a collection  or the mean
    of the values associated with each key in a collection of key-value pairs
    '''
    means_per_key = (
        p | beam.Create([(1, 36),(2, 91),(3, 33),(3, 11),(4, 67),])
          | beam.combiners.Mean.PerKey()
          | beam.Map(print)
    )
