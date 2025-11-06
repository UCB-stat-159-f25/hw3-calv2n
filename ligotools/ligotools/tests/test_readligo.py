from ligotools import read_hdf5

def test_read_hdf5_returns_tuple():
    hdf5_file = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    res = read_hdf5(hdf5_file, readstrain=False)
    assert type(res) == tuple

def test_read_hdf5_is_len_7():
    hdf5_file = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    res = read_hdf5(hdf5_file, readstrain=False)
    assert len(res) == 7
