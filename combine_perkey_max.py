import apache_beam as beam

with beam.Pipeline() as p:
    elements_with_min_value_per_key = (
        p | 'Create produce' >> beam.Create([
        (1, 36),
        (2, 91),
        (3, 33),
        (3, 11),
        (4, 67),
        ]) 
        | beam.CombinePerKey(max)
        | beam.Map(print)
    )