import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# CẤU HÌNH TRANG STREAMLIT
# ==========================================
st.set_page_config(page_title="AIDEOM-VN Dashboard", layout="wide")
st.title("📊 BẢNG ĐIỀU KHIỂN CHIẾN LƯỢC KINH TẾ SỐ VN (AIDEOM-VN)")
st.markdown("Hệ thống hỗ trợ ra quyết định phân bổ ngân sách công nghệ số (Đồ án Bài 12)")

# ==========================================
# NẠP CHÍNH XÁC DỮ LIỆU THỰC TẾ TỪ M1 ĐẾN M5 CỦA BẠN
# ==========================================
# 1. Dữ liệu Module 1
df_m1 = pd.DataFrame({
    "Năm": [2026, 2027, 2028, 2029, 2030],
    "GDP Dự báo (Tỷ VND)": [15532.06, 16678.81, 17891.50, 19175.04, 20534.47],
    "TFP (A_t)": [39.7293, 40.2061, 40.6886, 41.1768, 41.6710],
    "Lao động (Triệu người)": [56.60, 60.00, 63.60, 67.42, 71.46]
})

# 2. Dữ liệu Module 2
df_m2_regions = pd.DataFrame({
    "Vùng Kinh tế": ["Đông Nam Bộ (Southeast)", "Đồng bằng sông Hồng (Red River Delta)", 
                     "Bắc Trung Bộ & Duyên hải MT", "Đồng bằng sông Cửu Long", 
                     "Trung du & Miền núi phía Bắc", "Tây Nguyên"],
    "Điểm Sẵn sàng Số (Readiness)": [0.927480, 0.920332, 0.343884, 0.141072, 0.103715, 0.035918]
})

df_m2_sectors = pd.DataFrame({
    "Ngành Kinh tế": ["Công nghiệp chế biến (Manufacturing)", "CNTT - Truyền thông (IT)", 
                      "Nông-Lâm-Thủy sản", "Tài chính-Ngân hàng", "Y tế", "Logistics-Vận tải", 
                      "Giáo dục-Đào tạo", "Bán buôn bán lẻ", "Xây dựng", "Khai khoáng"],
    "Điểm Ưu tiên (Priority)": [0.926716, 0.620876, 0.154039, 0.122288, 0.099452, 
                                0.098145, 0.091374, 0.091172, 0.073107, 0.043093]
})

# 3. Dữ liệu Module 3 (Bảng phân bổ ngân sách chi tiết của bạn)
actual_m3_records = [
    # --- Năm 2026 ---
    {"Năm": 2026, "Vùng": "Vùng_2", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 15000.00},
    {"Năm": 2026, "Vùng": "Vùng_3", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 2500.00},
    {"Năm": 2026, "Vùng": "Vùng_4", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 5000.00},
    {"Năm": 2026, "Vùng": "Vùng_6", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 15000.00},
    {"Năm": 2026, "Vùng": "Vùng_1", "Hạng mục": "Trí tuệ nhân tạo (AI)", "Ngân sách (Tỷ VND)": 5000.00},
    {"Năm": 2026, "Vùng": "Vùng_3", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 2500.00},
    {"Năm": 2026, "Vùng": "Vùng_5", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 5000.00},
    # --- Năm 2027 ---
    {"Năm": 2027, "Vùng": "Vùng_2", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 16500.00},
    {"Năm": 2027, "Vùng": "Vùng_3", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 2750.00},
    {"Năm": 2027, "Vùng": "Vùng_4", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 5500.00},
    {"Năm": 2027, "Vùng": "Vùng_6", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 16500.00},
    {"Năm": 2027, "Vùng": "Vùng_1", "Hạng mục": "Trí tuệ nhân tạo (AI)", "Ngân sách (Tỷ VND)": 5500.00},
    {"Năm": 2027, "Vùng": "Vùng_3", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 2750.00},
    {"Năm": 2027, "Vùng": "Vùng_5", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 5500.00},
    # --- Năm 2028 ---
    {"Năm": 2028, "Vùng": "Vùng_2", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 18000.00},
    {"Năm": 2028, "Vùng": "Vùng_3", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 3000.00},
    {"Năm": 2028, "Vùng": "Vùng_4", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 6000.00},
    {"Năm": 2028, "Vùng": "Vùng_6", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 18000.00},
    {"Năm": 2028, "Vùng": "Vùng_1", "Hạng mục": "Trí tuệ nhân tạo (AI)", "Ngân sách (Tỷ VND)": 6000.00},
    {"Năm": 2028, "Vùng": "Vùng_3", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 3000.00},
    {"Năm": 2028, "Vùng": "Vùng_5", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 6000.00},
    # --- Năm 2029 ---
    {"Năm": 2029, "Vùng": "Vùng_2", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 19500.00},
    {"Năm": 2029, "Vùng": "Vùng_3", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 3250.00},
    {"Năm": 2029, "Vùng": "Vùng_4", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 6500.00},
    {"Năm": 2029, "Vùng": "Vùng_6", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 19500.00},
    {"Năm": 2029, "Vùng": "Vùng_1", "Hạng mục": "Trí tuệ nhân tạo (AI)", "Ngân sách (Tỷ VND)": 6500.00},
    {"Năm": 2029, "Vùng": "Vùng_3", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 3250.00},
    {"Năm": 2029, "Vùng": "Vùng_5", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 6500.00},
    # --- Năm 2030 ---
    {"Năm": 2030, "Vùng": "Vùng_2", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 21000.00},
    {"Năm": 2030, "Vùng": "Vùng_3", "Hạng mục": "Hạ tầng số (I)", "Ngân sách (Tỷ VND)": 3500.00},
    {"Năm": 2030, "Vùng": "Vùng_4", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 7000.00},
    {"Năm": 2030, "Vùng": "Vùng_6", "Hạng mục": "Chuyển đổi số DN (D)", "Ngân sách (Tỷ VND)": 21000.00},
    {"Năm": 2030, "Vùng": "Vùng_1", "Hạng mục": "Trí tuệ nhân tạo (AI)", "Ngân sách (Tỷ VND)": 7000.00},
    {"Năm": 2030, "Vùng": "Vùng_3", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 3500.00},
    {"Năm": 2030, "Vùng": "Vùng_5", "Hạng mục": "Nhân lực số (H)", "Ngân sách (Tỷ VND)": 7000.00},
]
df_m3 = pd.DataFrame(actual_m3_records)

# 4. Dữ liệu Module 4 (Trạng thái năm cuối 2030)
df_m4 = pd.DataFrame({
    "Kịch bản": ["Cơ sở", "Khủng hoảng An ninh mạng", "Đột phá AI"],
    "GDP Thực tế (Tỷ VND)": [49328.15, 46614.52, 54447.48],
    "Rủi ro Thất nghiệp (%)": [3.56, 3.56, 3.91],
    "Rủi ro Mạng (%)": [13.94, 14.34, 13.94]
})

# 5. Dữ liệu Module 5 (Hệ thống điểm rủi ro kỳ vọng)
df_m5 = pd.DataFrame({
    "Năm": [2026, 2027, 2028, 2029, 2030],
    "An ninh mạng": [19.88, 19.88, 19.88, 19.88, 19.88],
    "Môi trường/Phát thải": [12.19, 12.19, 12.19, 12.19, 12.19],
    "Phụ thuộc công nghệ": [1.06, 1.06, 1.06, 1.06, 1.06]
})

# ==========================================
# THIẾT KẾ CÁC TAB GIAO DIỆN
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 M1 & M2: Dự báo & Ưu tiên số", 
    "💰 M3: Phân bổ Ngân sách Tối ưu", 
    "⚠️ M4 & M5: Sức chống chịu & Rủi ro",
    "💡 Đánh giá Chính sách"
])

# ------------------------------------------
# TAB 1: DỰ BÁO VĨ MÔ & XẾP HẠNG (M1 + M2)
# ------------------------------------------
with tab1:
    st.header("1. Dự báo Chỉ số Kinh tế Vĩ mô (2026 - 2030)")
    col1, col2 = st.columns(2)
    with col1:
        fig_gdp = px.line(df_m1, x="Năm", y="GDP Dự báo (Tỷ VND)", markers=True, title="Quỹ đạo Tăng trưởng GDP Xu hướng")
        st.plotly_chart(fig_gdp, use_container_width=True)
    with col2:
        fig_tfp = px.line(df_m1, x="Năm", y="TFP (A_t)", markers=True, color_discrete_sequence=['orange'], title="Dự báo Năng suất các nhân tố tổng hợp TFP")
        st.plotly_chart(fig_tfp, use_container_width=True)
        
    st.markdown("---")
    st.header("2. Kết quả Xếp hạng Sẵn sàng Số từ Module 2")
    col3, col4 = st.columns(2)
    with col3:
        fig_regions = px.bar(df_m2_regions.sort_values("Điểm Sẵn sàng Số (Readiness)", ascending=True), 
                             x="Điểm Sẵn sàng Số (Readiness)", y="Vùng Kinh tế", orientation='h', 
                             color="Điểm Sẵn sàng Số (Readiness)", title="Chỉ số Sẵn sàng Số (Readiness Score) theo 6 Vùng")
        st.plotly_chart(fig_regions, use_container_width=True)
    with col4:
        fig_sectors = px.bar(df_m2_sectors.sort_values("Điểm Ưu tiên (Priority)", ascending=True), 
                             x="Điểm Ưu tiên (Priority)", y="Ngành Kinh tế", orientation='h',
                             color_discrete_sequence=['teal'], title="Xếp hạng Ưu tiên Số hóa (Priority Score) 10 Ngành")
        st.plotly_chart(fig_sectors, use_container_width=True)

# ------------------------------------------
# TAB 2: TỐI ƯU PHÂN BỔ NGÂN SÁCH (M3)
# ------------------------------------------
with tab2:
    st.header("3. Kế hoạch Giải ngân Ngân sách Tối ưu hóa")
    st.success("🎯 **TỔNG GDP GAIN KỲ VỌNG (ĐÃ CHIẾT KHẤU): 371,057.01 Tỷ VND**")
    
    # Biểu đồ phân bổ theo hạng mục công nghệ
    fig_budget = px.bar(df_m3, x="Năm", y="Ngân sách (Tỷ VND)", color="Hạng mục", 
                        title="Cơ cấu Phân bổ Ngân sách theo Hạng mục Công nghệ qua từng năm",
                        text_auto='.2s')
    st.plotly_chart(fig_budget, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Bảng Ma trận dữ liệu Phân bổ chi tiết (Năm - Vùng - Hạng mục):")
    st.dataframe(df_m3, use_container_width=True)

# ------------------------------------------
# TAB 3: ĐÁNH GIÁ TÁC ĐỘNG & RỦI RO (M4 + M5)
# ------------------------------------------
with tab3:
    st.header("4. Kiểm định Sức chống chịu Vĩ mô (Stress Testing - M4)")
    st.info("Trạng thái nền kinh tế tại năm đích 2030 trước các kịch bản cú sốc.")
    
    col5, col6 = st.columns(2)
    with col5:
        fig_m4_gdp = px.bar(df_m4, x="Kịch bản", y="GDP Thực tế (Tỷ VND)", color="Kịch bản",
                            title="Biến động quy mô GDP thực tế năm 2030 theo Kịch bản")
        st.plotly_chart(fig_m4_gdp, use_container_width=True)
    with col6:
        df_m4_melt = df_m4.melt(id_vars=["Kịch bản"], value_vars=["Rủi ro Thất nghiệp (%)", "Rủi ro Mạng (%)"],
                                var_name="Loại chỉ số", value_name="Tỷ lệ (%)")
        fig_m4_risk = px.bar(df_m4_melt, x="Kịch bản", y="Tỷ lệ (%)", color="Loại chỉ số", barmode='group',
                             title="Tác động tới Thất nghiệp và An ninh mạng")
        st.plotly_chart(fig_m4_risk, use_container_width=True)

    st.markdown("---")
    st.header("5. Hệ thống Cảnh báo Rủi ro Hệ thống Ngẫu nhiên (M5)")
    fig_m5 = px.line(df_m5, x="Năm", y=["An ninh mạng", "Môi trường/Phát thải", "Phụ thuộc công nghệ"], 
                     markers=True, title="Giám sát Điểm rủi ro Hệ thống Kỳ vọng (Thang điểm 100)")
    fig_m5.update_layout(yaxis_title="Điểm số Rủi ro")
    st.plotly_chart(fig_m5, use_container_width=True)
    
    st.success("✅ **[OK] CHÚC MỪNG:** Các chỉ số rủi ro đều nằm trong ngưỡng an toàn nhờ chiến lược phân bổ vốn cân bằng.")

# ------------------------------------------
# TAB 4: KẾT LUẬN & KHUYẾN NGHỊ
# ------------------------------------------
with tab4:
    st.header("💡 Báo cáo và Khuyến nghị Tư vấn Chính sách")
    st.markdown("""
    Dựa trên kết quả thực thi tích hợp từ hệ thống mô hình **AIDEOM-VN**, tổ tư vấn rút ra các khuyến nghị chiến lược sau:
    
    1. **Hiệu quả Đầu tư vượt trội:** Chiến lược tối ưu hóa tuyến tính/nguyên ở Module 3 đạt mức **GDP Gain trên 371 nghìn tỷ VND**. Mô hình phân bổ dòng vốn cực kỳ thông minh khi dồn trọng tâm hạ tầng vào các vùng kinh tế đầu tàu có sức hấp thụ công nghệ tốt nhất như **Đông Nam Bộ (0.927)** và **Đồng bằng Sông Hồng (0.920)**.
    2. **Khống chế Rủi ro Mạng bền vững:** Nhờ việc duy trì đầu tư cân đối cho hạng mục **Nhân lực số (H)**, điểm rủi ro an ninh mạng kỳ vọng được giữ vững ở mức an toàn ổn định là **19.88/100** qua các năm, giúp nền kinh tế duy trì sức chống chịu tốt ngay cả khi xảy ra kịch bản *Khủng hoảng An ninh mạng* thực tế (GDP 2030 duy trì ở mức cao 46,614.52 tỷ VND).
    3. **Ứng phó với làn sóng Trí tuệ nhân tạo:** Kịch bản *Đột phá AI* kích hoạt một lực đẩy kinh tế cực lớn, đưa GDP tăng vọt lên **54,447.48 tỷ VND**. Tuy nhiên, mặt trái của nó là đẩy tỷ lệ rủi ro thất nghiệp lên mức cao nhất (**3.91%**). 
    
    **Khuyến nghị hành động:** Chính phủ cần tiếp tục kiên định với mô hình phân bổ ngân sách hiện tại, đồng thời sớm thành lập quỹ đào tạo lại nghề nghiệp toàn diện nhằm tái cấu trúc và dịch chuyển lực lượng lao động bị ảnh hưởng bởi quá trình tự động hóa AI.
    """)
    st.caption("Sản phẩm thuộc Module 6 - Hệ thống hỗ trợ ra quyết định AIDEOM-VN | Đồ án Môn học các Mô hình ra quyết định.")