# ROS 2 Workspace — Yahboom ROSMASTER X3

ROS 2 Jazzy + Gazebo Harmonic 기반 Yahboom ROSMASTER X3 메카넘 휠 AMR 시뮬레이션 워크스페이스.

## 환경

- ROS 2 Jazzy (Ubuntu Noble 24.04)
- Gazebo Harmonic (gz-sim 8)
- 물리 엔진: DART (`gz-physics-dartsim-plugin`)

---

## 새 컴퓨터 필수 설정

> [!warning] 새 컴퓨터 필수 작업
> `gz.transport13` Python 바인딩은 ROS 2 Jazzy / Gazebo Harmonic apt 패키지에 **포함되어 있지 않다.**
> 설치하지 않으면 `gz_pose_tf_publisher`가 Gazebo 포즈 구독에 실패하고, RViz에 `map` 프레임이 나타나지 않는다.

---

### 설치 절차

**Step 1.** gz-transport13 소스 클론

```bash
git clone --depth 1 --branch gz-transport13 https://github.com/gazebosim/gz-transport.git /tmp/gz-transport-src
```

**Step 2.** Python 바인딩 빌드

```bash
cmake -B /tmp/gz-transport-src/python/build -S /tmp/gz-transport-src/python -DCMAKE_BUILD_TYPE=Release
cmake --build /tmp/gz-transport-src/python/build --parallel $(nproc)
cmake --install /tmp/gz-transport-src/python/build --prefix /tmp/gz-transport-install
```

**Step 3.** user site-packages에 설치

```bash
SITE=$(python3 -c "import site; print(site.getusersitepackages())")
mkdir -p "$SITE/gz/transport13"
cp /tmp/gz-transport-install/lib/python/gz/transport13/_transport.cpython-*.so "$SITE/gz/transport13/"
cp /tmp/gz-transport-install/lib/python/gz/transport13/__init__.py "$SITE/gz/transport13/"
```

**Step 4.** gz.msgs10 경로를 ~/.bashrc에 추가

```bash
echo 'export PYTHONPATH="/opt/ros/jazzy/opt/gz_msgs_vendor/lib/python:$PYTHONPATH"' >> ~/.bashrc
source ~/.bashrc
```

**Step 5.** 정상 설치 확인

```bash
python3 -c "import gz.transport13; import gz.msgs10.pose_v_pb2; print('OK')"
```

---

## 빌드 및 실행

```bash
# 빌드
colcon build
source install/setup.bash

# 시뮬레이션 실행 (factory map)
bash src/yahboom_rosmaster/yahboom_rosmaster_bringup/scripts/rosmaster_x3_gazebo_2.sh
```

---

## 권장 ~/.bashrc 설정

아래를 `~/.bashrc` 하단에 추가한다. `# ← 변경` 표시된 항목은 본인 환경에 맞게 수정.

```bash
# ── Aliases ────────────────────────────────────────────────
alias sb="source ~/.bashrc; echo \"bashrc is reloaded\""
alias ros_domain="export ROS_DOMAIN_ID=13; echo \"ROS_DOMAIN_ID=13\""          # ← 변경: ROS_DOMAIN_ID
alias jazzy="source /opt/ros/jazzy/setup.bash; export ROS_DOMAIN_ID=13; echo \"Ros2 Jazzy is activated (DOMAIN_ID=13)!\""  # ← 변경: ROS_DOMAIN_ID
alias sisb="source ~/ajm_ws/install/setup.bash; echo \"Local workspace activated!\""           # ← 변경: 워크스페이스 경로
alias build="cd ~/ajm_ws && colcon build && source ~/ajm_ws/install/setup.bash; echo \"Build & Source completed!\""        # ← 변경: 워크스페이스 경로
alias x3="bash ~/ajm_ws/src/yahboom_rosmaster/yahboom_rosmaster_bringup/scripts/rosmaster_x3_gazebo_2.sh"                  # ← 변경: 워크스페이스 경로
alias xslam="bash ~/ajm_ws/src/yahboom_rosmaster/yahboom_rosmaster_bringup/scripts/rosmaster_x3_gazebo_slam.sh"            # ← 변경: 워크스페이스 경로
alias bc="code ~/.bashrc"
alias yahboom='ros2 launch urdf_tutorial display.launch.py model:=/home/smoc/ajm_ws/src/yahboom_rosmaster/yahboom_rosmaster_description/urdf/robots/rosmaster_x3.urdf.xacro'  # ← 변경: /home/smoc → 본인 홈 디렉토리

# ── ROS 2 auto-source ──────────────────────────────────────
source /opt/ros/jazzy/setup.bash
echo "ROS2 activated"
echo "ROS_DOMAIN_ID=13"                                                          # ← 변경: ROS_DOMAIN_ID
[ -f ~/ajm_ws/install/setup.bash ] && source ~/ajm_ws/install/setup.bash        # ← 변경: 워크스페이스 경로
echo "sourcing done, ajm_ws/install/setup.bash"

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export PATH="$HOME/.local/bin:$PATH"
export PYTHONPATH="/opt/ros/jazzy/opt/gz_msgs_vendor/lib/python:$PYTHONPATH"
```
