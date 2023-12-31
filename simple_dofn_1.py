import apache_beam as beam

# Output PCollection
class Output(beam.PTransform):
    class _OutputFn(beam.DoFn):
        def __init__(self, prefix=''):
            super().__init__()
            self.prefix = prefix

        def process(self, element):
            print(self.prefix+str(element))

    def __init__(self, label=None,prefix=''):
        super().__init__(label)
        self.prefix = prefix

    def expand(self, input):
        input | beam.ParDo(self._OutputFn(self.prefix))

# Multiplications by 10
class MultiplyByTenDoFn(beam.DoFn):
    '''
    DoFns - they’re what define your pipeline’s exact data processing tasks. DoFn is a Beam SDK class that defines distribute processing function.
    When you apply a ParDo Transform,  you will need to provide the user code  in the form of a DoFn object.
    '''
    def process(self, element):
        yield element * 10 /2


with beam.Pipeline() as p:
  (p | beam.Create([1, 2, 3, 4, 5])
    # Transform simple DoFn operation
     | beam.ParDo(MultiplyByTenDoFn()) #Extract the fields from the PCollection  and makes computations on every element of the PCollection, outputing the result as a new PCollection
     | Output())