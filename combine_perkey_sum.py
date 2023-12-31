import apache_beam as beam

with beam.Pipeline() as p:
    '''
    Count all elements of the array.  find the global sum value from the PCollection by using CombineGlobally(sum)
    '''
    totals_per_key = (
        p | 'Create produce' >> beam.Create([
            ('🥕', 3),
            ('🥕', 2),
            ('🍆', 1),
            ('🍅', 4),
            ('🍅', 5),
            ('🍅', 3),])
        | 'Sum values per key' >> beam.CombinePerKey(sum)
        | beam.Map(print))
