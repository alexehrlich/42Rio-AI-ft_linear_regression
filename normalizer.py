class DataNormalizer:
	def __init__(self, df) -> None:
		self.km_mean = 0.0
		self.km_std = 0.0
		self.price_mean = 0.0
		self.price_std = 0.0
		self.df = df
		self.normalized_df = df.copy()

	# Normalize the data using the 'Standardization' technique
	# Setting the mean value to 0 and the standard deviation to 1.
	# Normalization is needed when the range in the data set differs a lot, 
	# which can lead to bad/no convergence of the algorithm
	def normalize(self):
		self.km_mean = self.df['km'].mean()
		self.km_std = self.df['km'].std()
		self.price_mean = self.df['price'].mean()
		self.price_std = self.df['price'].std()
		self.normalized_df = self.df.copy()
		self.normalized_df['km'] = (self.df['km'] - self.km_mean) / self.km_std
		self.normalized_df['price'] = (self.df['price'] - self.price_mean) / self.price_std

		return self.normalized_df

	def denormalize_thetas(self, n_theta0, n_theta1):
		theta1_original = n_theta1 * self.price_std / self.km_std
		theta0_original = self.price_mean + (n_theta0 * self.price_std) - (theta1_original * self.km_mean)

		return theta0_original, theta1_original
