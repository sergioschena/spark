#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import unittest
from pyspark.sql.tests.pandas.test_pandas_udf_scalar import ScalarPandasUDFTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase


class PandasUDFScalarParityTests(ScalarPandasUDFTestsMixin, ReusedConnectTestCase):
    def test_nondeterministic_vectorized_udf_in_aggregate(self):
        self.check_nondeterministic_analysis_exception()

    @unittest.skip("Spark Connect doesn't support RDD but the test depends on it.")
    def test_vectorized_udf_empty_partition(self):
        super().test_vectorized_udf_empty_partition()

    @unittest.skip("Spark Connect doesn't support RDD but the test depends on it.")
    def test_vectorized_udf_struct_with_empty_partition(self):
        super().test_vectorized_udf_struct_with_empty_partition()

    # TODO(SPARK-48086): Reenable this test case
    @unittest.skipIf(
        "SPARK_SKIP_CONNECT_COMPAT_TESTS" in os.environ, "Failed with different Client <> Server"
    )
    def test_vectorized_udf_exception(self):
        self.check_vectorized_udf_exception()

    def test_vectorized_udf_nested_struct(self):
        self.check_vectorized_udf_nested_struct()

    def test_vectorized_udf_return_scalar(self):
        self.check_vectorized_udf_return_scalar()

    def test_scalar_iter_udf_close(self):
        self.check_scalar_iter_udf_close()

    # TODO(SPARK-43727): Parity returnType check in Spark Connect
    @unittest.skip("Fails in Spark Connect, should enable.")
    def test_vectorized_udf_wrong_return_type(self):
        self.check_vectorized_udf_wrong_return_type()

    def test_vectorized_udf_invalid_length(self):
        self.check_vectorized_udf_invalid_length()


if __name__ == "__main__":
    from pyspark.sql.tests.connect.test_parity_pandas_udf_scalar import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
