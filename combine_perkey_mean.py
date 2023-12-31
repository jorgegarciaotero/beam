import apache_beam as beam

with beam.Pipeline() as p:
    elements_with_min_value_per_key = (
        p | 'Create produce' >> beam.Create([
        ('🥕', 3),
        ('🥕', 2),
        ('🍆', 1),
        ('🍅', 4),
        ('🍅', 5),
        ('🍅', 3),])
        | 'Get min value per key' >> beam.CombinePerKey(min)
        | beam.Map(print)
    )