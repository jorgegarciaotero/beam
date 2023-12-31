import apache_beam as beam

with beam.Pipeline() as p:
    '''
     global sum value from the PCollection by using CombineGlobally(sum)
    '''
    total = (
        p | 'Create numbers' >> beam.Create([3, 4, 1, 2])
        | 'Sum values' >> beam.CombineGlobally(sum)
        | beam.Map(print))
