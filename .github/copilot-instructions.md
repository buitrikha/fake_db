# Copilot Instructions for fake_db

## Project Overview
A Python-based data generation tool that creates realistic fake student management system data for a Vietnamese university (QLSINHVIEN database). Uses the Faker library with Vietnamese locale and mysql-connector-python to populate a relational database schema with interconnected entities.

## Architecture & Data Model

### Core Concept
Sequential hierarchical data generation where each entity depends on previously generated entities:
1. **KHOA (Departments)** - 10 base units
2. **BOMON (Subject Groups)** - 30 units, each linked to a department
3. **GIANGVIEN (Lecturers)** - 200 records, assigned to subject groups
4. **MONHOC (Courses)** - 100 courses, distributed across subject groups
5. **LOPHANHCHINH (Administrative Classes)** - 50 classes per department
6. **SINHVIEN (Students)** - 1000 students per administrative class
7. **HOCKY (Semesters)** - 10 semesters spanning 5 academic years (2020-2025)
8. **LOPHOCPHAN (Class Sessions)** - 300 teaching sessions per semester
9. **DANGKY (Enrollments)** - 2000 student-session registrations
10. **DIEM (Grades)** - 1500 grade records (subset of enrollments)

### Key Patterns
- **Referential Integrity**: Each level maintains lists of IDs (`khoa_list`, `bomon_list`, etc.) for random FK assignment
- **ID Convention**: Sequential IDs with type prefixes (e.g., `K01`, `BM02`, `GV0001`, `SV00001`)
- **Uniqueness via Sets**: `dangky_set` prevents duplicate student-session enrollments
- **Sampling Strategy**: Grades drawn from enrollment set using `random.sample()` to ensure subset relationship

## Critical Workflow

### Running the Data Generation
```bash
python generate_fake_db.py
```

**Prerequisites:**
- MySQL server running on localhost:3306
- Database `QLSINHVIEN` exists with proper schema
- Credentials: user=`root`, password=`kha11` (hardcoded in script)

**Process Flow:**
- Script commits after each entity type (10 separate transactions)
- Console output shows progress: "Đang tạo dữ liệu [ENTITY]..."
- Final summary displays totals for all 10 entity types
- Execution order is critical—do not reorder entity generations

### Database Connection Details
Located at lines 9-15. Hardcoded connection parameters:
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: `kha11`
- Database: `QLSINHVIEN`

**Note:** Credentials are exposed in source. Use environment variables for production.

## Project-Specific Conventions

### Naming Patterns (Vietnamese Context)
- **Entity Fields**: Suffixed with type (e.g., `_SV` for student fields, `_GV` for lecturer, `_MH` for course)
- **Status Codes**: Vietnamese text values (`'Đang học'`, `'Bảo lưu'`, `'Tốt nghiệp'` for student status)
- **Gender**: Vietnamese values `'Nam'` (Male), `'Nữ'` (Female)

### Data Generation Assumptions
- **Age Ranges**: Lecturers 30-65 years, students 18-25 years (lines 97-98, 172)
- **Credit Hours**: Fixed choices: 30, 45, 60 for lectures; 0, 15, 30 for practical (line 143)
- **Grades**: Floating-point 0-10 scale; midterm/final weighted separately from attendance (lines 280-283)
- **Academic Years**: Auto-calculated from semester index (2020-2025), split into semesters 1-2 per year
- **Room Assignments**: Fixed pool of 8 rooms (A101, A102, B201, B202, C301, C302, D401, D402)

### Faker Library Usage
- **Locale**: `'vi_VN'` for Vietnamese names, addresses, phone numbers
- **Methods Used**:
  - `fake.name()` - Vietnamese names
  - `fake.date_of_birth()` - Age-constrained birth dates
  - `fake.phone_number()` - Vietnamese phone formats
  - `fake.address()` - Vietnamese addresses

## Integration Points & Dependencies

### External Dependencies
1. **mysql-connector-python** - Direct MySQL connection (not SQLAlchemy ORM)
2. **faker** - Data generation with Vietnamese locale
3. **random** - Seeded randomization across all selections
4. **datetime** - Semester date calculations (lines 215-222)

### Database Schema Expectations
Requires pre-existing tables with exact names:
- KHOA, BOMON, GIANGVIEN, MONHOC, LOPHANHCHINH, SINHVIEN, HOCKY, LOPHOCPHAN, DANGKY, DIEM

No schema creation occurs in this script—it assumes DDL already exists.

### No Error Handling
Script contains **zero exception handling**. Any database errors will crash execution. Connection must be manually closed if interrupted.

## Extending the Script

### Adding New Entity Types
1. Create a list to store IDs (e.g., `newen_list = []`)
2. Insert in appropriate position (respect FK dependencies)
3. Add commit after insertion loop
4. Add console feedback and final summary line

### Modifying Data Volume
Entity counts are hardcoded in `range()` calls:
- Departments: `range(10)` → line 25
- Subject Groups: `range(30)` → line 52
- Lecturers: `range(200)` → line 78
- Courses: `range(100)` → line 114
- Administrative Classes: `range(50)` → line 166
- Students: `range(1000)` → line 183
- Semesters: `range(10)` → line 205
- Class Sessions: `range(300)` → line 227
- Enrollments: `2000` registrations → line 255
- Grades: `1500` records → line 269

### Common Issues
- **Duplicate Enrollment Attempts**: `dangky_set` uses tuple keys. If limit too low, infinite loop risk in while condition (lines 254-257).
- **Cascade Delete**: Modifying department count requires recalculation of dependent class counts.
- **Foreign Key Violations**: Ensure all FK references point to generated IDs from prior steps.

## When Modifying

- Preserve transaction commit pattern (after each entity block)
- Maintain ID format conventions for consistency
- Test with small counts first (e.g., `range(5)` for departments)
- Verify schema changes don't break INSERT statements
- Update console print messages and final summary when adding/removing entities
