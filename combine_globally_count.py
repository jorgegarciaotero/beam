import apache_beam as beam

with beam.Pipeline() as p:
    '''
    Count.Globally() to count all elements in a PCollection, even if there are duplicate elements.
    '''
    total_elements = (
        p | 'Create plants' >> beam.Create(['🍓', '🥕', '🥕', '🥕', '🍆', '🍆', '🍅', '🍅', '🍅', '🌽'])
        | 'Count all elements' >> beam.combiners.Count.Globally()
        | beam.Map(print))