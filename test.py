from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

fastf1.plotting.setup_mpl()
fastf1.Cache.enable_cache('cache')
# session = fastf1.get_session(2019, 'Monza', 'Q')
reace_year = 2022
reace_round = "Azerbaijan"
session = fastf1.get_session(reace_year, reace_round, "Q")
session.load()
laps_lec = session.laps.pick_driver(77)
laps_ham = session.laps.pick_driver(24)
fast_leclerc = laps_lec.pick_fastest()
fast_HAM = laps_ham.pick_fastest()
lec_car_data = fast_leclerc.get_car_data().add_distance()
ham_car_data = fast_HAM.get_car_data().add_distance()
# print(laps_ham[laps_ham["LapNumber"] == 4].iloc[0])
# exit()

title_77 = fast_leclerc["Driver"] + " " +  str(fast_leclerc["LapTime"])[11:19] + "  " +  str(fast_leclerc["Sector1Time"])[13:19] + "  " +  str(fast_leclerc["Sector2Time"])[13:19] + "  " +  str(fast_leclerc["Sector3Time"])[13:19] + "  " +  fast_leclerc["Compound"]
title_24 = fast_HAM["Driver"] + " " +  str(fast_HAM["LapTime"])[11:19] + "  " +  str(fast_HAM["Sector1Time"])[13:19] + "  " +  str(fast_HAM["Sector2Time"])[13:19] + "  " +  str(fast_HAM["Sector3Time"])[13:19] + "  " +  fast_HAM["Compound"]
# a = fast_HAM.get_pos_data()
# b = fast_leclerc.get_weather_data()
# c = fast_leclerc.get_telemetry()
if (fast_HAM["LapTime"] > fast_leclerc["LapTime"]):
    gap_time = fast_HAM["LapTime"] - fast_leclerc["LapTime"]
else:
    gap_time = fast_leclerc["LapTime"] - fast_HAM["LapTime"]
gap_time_sec = gap_time.seconds
gap_time_mic = gap_time.microseconds
vCar = lec_car_data['Throttle']
vH = ham_car_data["Throttle"]
if (fast_HAM["LapTime"] > fast_leclerc["LapTime"]):
    label_77 = "BOT " + str(fast_leclerc["LapTime"])[11:19]
    label_24 = "ZHO +" + str(gap_time_sec) + "." + str(gap_time_mic)[0:3]
else:
    label_77 = "BOT +" + str(gap_time_sec) + "." + str(gap_time_mic)[0:3]
    label_24 = "ZHO " + str(fast_HAM["LapTime"])[11:19]

fig, ax = plt.subplots(nrows=5, ncols=1, figsize=(35, 15), dpi=150)
# fig.add_gridspec(nrows=5, ncols=1, width_ratios=[1,1,1,1,1], height_ratios=[2,1,1,1,1])
fig.suptitle("F1 " + str(reace_year) + "/ " + reace_round + "/ " + "排位赛 / " + "Bot-ZHO", fontsize=18)
ax[0].plot(lec_car_data["Distance"], lec_car_data["Speed"], color="red", label=label_77 )
ax[0].plot(ham_car_data["Distance"], ham_car_data["Speed"], color="blue", label=label_24)
# ax[0].set_xlabel("时间")
ax[0].set_ylabel('速度 [Km/h]')
ax[0].set_title(title_77 + "\n" + title_24, fontsize=13)
ax[0].legend(loc='upper right')
# fig, ax2 = plt.subplots()
ax[1].plot(lec_car_data["Distance"], vCar, color="red", label=label_77)
ax[1].plot(ham_car_data["Distance"], vH, color="blue", label=label_24)
# ax[1].set_xlabel("时间")
ax[1].set_ylabel('油门 100%')
# ax[1].set_title('速度')
# ax2.legend()
# fig, ax3 = plt.subplots()
ax[2].plot(lec_car_data["Distance"], lec_car_data["Brake"], color="red", label=label_77 )
ax[2].plot(ham_car_data["Distance"], ham_car_data["Brake"], color="blue", label=label_24)
ax[2].set_ylabel('刹车')

ax[3].plot(lec_car_data["Distance"], lec_car_data["RPM"], color="red", label=label_77 )
ax[3].plot(ham_car_data["Distance"], ham_car_data["RPM"], color="blue", label=label_24)
ax[3].set_ylabel('RPM')

ax[4].plot(lec_car_data["Distance"], lec_car_data["nGear"], color="red", label=label_77 )
ax[4].plot(ham_car_data["Distance"], ham_car_data["nGear"], color="blue", label=label_24)
ax[4].set_xlabel("Distance")
ax[4].set_ylabel('档位')

# ax[2].set_title('刹车')
# ax[2,:].legend()
fig.tight_layout(h_pad=1)
plt.subplots_adjust(top=0.9)
plt.savefig("./reace_data/{}_fastLap.png".format(reace_round))
plt.show()