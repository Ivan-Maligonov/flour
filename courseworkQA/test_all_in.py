import requests
import pytest
import test_1_checking_the_leftovers as t1
import test_2_post_order_28112021 as t2
import test_3_post_rus_status as t3
import test_4_order_auto_id as t4
import test_5_order_max_id_500 as t5
import test_6_delete_all_negative as t6
import test_7_petID_400_negative as t7
import test_8_shipdate_500_negative as t8
import test_9_idnameorder_negative as t9
import test_10_order_id_minus_negative as t10
import test_11_order_id_drobi_negative as t11
import test_12_quantity_max9_negativ as t12


t1.test_checking_the_leftovers_get_positive()
t2.test_order_POST()
t2.test_get_order()
t2.test_Delete_28112021()
t2.test_get_after_del()
t3.test_order_POST_rus_status()
t3.test_get_order()
t3.test_Delete_POST_rus_status()
t3.test_get_after_del()
t4.test_order_auto_id()
t4.test_get_order()
t4.test_Delete_order_auto_id()
t4.test_get_after_del()
t5.test_order_max_id_500()
t6.test_delete_all_negative()
t6.test_get_order()
t7.test_petID_400_negative()
t8.test_shipDate_500_negative()
t9.test_idnameorder_negative()
t10.test_order_id_negative()
t10.test_get_order()
t11.test_order_id_2_2_negative()
t11.test_order_2_9_negative()
t11.test_order_id_5_5_negative()
t11.test_order_petid_drobi_negative()
t11.test_order_quantity_drobi_negative()
t12.test_quantity_max9_negativ()
