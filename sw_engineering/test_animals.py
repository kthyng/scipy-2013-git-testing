import animals


def test_read_animals():
	ref_dates = ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']
	ref_times = ['21:06', '14:12', '10:24', '20:08', '18:46']
	ref_species = ['Grizzly', 'Elk', 'Elk', 'Wolverine', 'Muskox']
	ref_counts = [36, 25, 26, 31, 20]

	dates, times, species, counts = animals.read_animals('animals.txt')

	assert dates == ref_dates
	assert times == ref_times
	assert counts == ref_counts
	assert species == ref_species
    