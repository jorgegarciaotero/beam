import apache_beam as beam

def is_perennial(plant):
    '''
    Returns True if the plant is perennial.
    '''
    return plant['duration'] == 'perennial'

with beam.Pipeline() as p:
    '''
    Example of pipeline. 
    First stem create the PCollection with the plants.
    Second stem filter the plants that are perennial.
    Third stem print the plants.
    '''
    perennials = (
        p | 'Gardening plants' >> beam.Create([
            {
                'icon': '🍓', 'name': 'Strawberry', 'duration': 'perennial'
            },
            {
                'icon': '🥕', 'name': 'Carrot', 'duration': 'biennial'
            },
            {
                'icon': '🍆', 'name': 'Eggplant', 'duration': 'perennial'
            },
            {
                'icon': '🍅', 'name': 'Tomato', 'duration': 'annual'
            },
            {
                'icon': '🥔', 'name': 'Potato', 'duration': 'perennial'
            },
        ])
        | 'Filter perennials' >> beam.Filter(is_perennial)
        | beam.Map(print))
