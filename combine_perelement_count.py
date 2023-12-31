import apache_beam as beam

with beam.Pipeline() as p:
    '''
    Count all elements of the array
    '''
    total_unique_elements = (
        p | 'Create produce' >> beam.Create(['🍓', '🥕', '🥕', '🥕', '🍆', '🍆', '🍅', '🍅', '🍅', '🌽'])
        | 'Count unique elements' >> beam.combiners.Count.PerElement()
        | beam.Map(print))
