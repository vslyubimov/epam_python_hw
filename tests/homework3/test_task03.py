from homework3.task03 import make_filter, sample_data


def test_main_result():
    result = [{'is_dead': True, 'kind': 'parrot',
               'type': 'bird', 'name': 'polly'}]
    assert make_filter(name='polly', type='bird').apply(sample_data) == result

    # add more tests about bugs
