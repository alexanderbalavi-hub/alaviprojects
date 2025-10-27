import pandas as pd
import pytest
from uebung.createdataframe import sample_df
# Sample DataFrame for testing

def test_location(sample_df):
    result = sample_df.loc[['r1', 'r2'], ['c1', 'c2']]
    expected = pd.DataFrame({'c1': [0.1, 0.5], 'c2': [0.4, 0.2]}, index=['r1', 'r2'])
    pd.testing.assert_frame_equal(result, expected)

def test_area(sample_df):
    result = sample_df[2:4]
    expected = pd.DataFrame(
        {'c1': [0.8, 0.3], 'c2': [0.9, 0.6], 'c3': [0.1, 0.8]},
        index=['r3', 'r4']
    )
    pd.testing.assert_frame_equal(result, expected)

def test_filter(sample_df):
    result = sample_df < 0.2
    expected = pd.DataFrame(
        {'c1': [True, False, False, False], 'c2': [False, False, False, False], 'c3': [False, False, True, False]},
        index=['r1', 'r2', 'r3', 'r4']
    )
    pd.testing.assert_frame_equal(result, expected)

def test_shape(sample_df):
    assert sample_df.shape == (4, 3)

def test_column_names(sample_df):
    assert list(sample_df.columns) == ['c1', 'c2', 'c3']

def test_row_names(sample_df):
    assert list(sample_df.index) == ['r1', 'r2', 'r3', 'r4']