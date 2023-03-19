<template>
  <div class="member-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>成员</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberName" type="text"
               placeholder="请输入姓名"/>
      <n-input style="width: 600px; margin-right: 10px;" v-model:value="memberNo" type="text" placeholder="请输入工号, 与其他条件互斥"/>
      <n-input style="width: 350px; margin-right: 10px;" v-model:value="memberGroup" type="text"
               placeholder="请输入组"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberPhone" type="text"
               placeholder="请输入手机号码"/>
      <n-input style="width: 400px; margin-right: 10px;" v-model:value="memberEmail" type="text"
               placeholder="请输入工作邮箱"/>
      <n-select style="width: 350px; margin-right: 10px;" :options="memberSexSelectOptions" placeholder="请选择性别"/>
      <n-input style="margin-right: 10px;" v-model:value="memberArchGroup" type="text"
               placeholder="请输入组织架构, 支持全文检索.."/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info" @click="handleSearchButtonClicked">
            <template #icon>
              <n-icon>
                <search-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>按照指定条件进行搜索</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="success" @click="handleAddButtonClicked">
            <template #icon>
              <n-icon>
                <plus-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>添加</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="warning"
                    @click="handleBatchDeleteButtonClicked">
            <template #icon>
              <n-icon>
                <delete-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>删除选中的条目</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="error" @click="handleBatchEmptyButtonClicked">
            <template #icon>
              <n-icon>
                <close-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>清空搜索条件</span>
      </n-tooltip>
    </div>
    <n-data-table striped :columns="columns" :data="accounts" :pagination="pagination" @update:checked-row-keys="handleUpdateCheckedRowKeys"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加成员"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input v-model:value="useCreateByName" type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">工号</div>
          <n-input v-model:value="useCreateByNo" type="text" placeholder="必填, 请输入工号" style="margin-bottom: 10px; max-width: 250px"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
<!--          <n-select v-model:value="useCreateByGroup" placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"/>-->
          <n-input v-model:value="useCreateByGroup" placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select v-model:value="useCreateBySex" :options="roleSelectOptions" placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input v-model:value="useCreateByPhone" type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input v-model:value="useCreateByEmail" type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input v-model:value="useCreateByArchGroup" type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowDetailModal" :mask-closablef="false" preset="card" title="Z12831839 的详细信息"
             :on-after-leave="onDetailModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input v-model:value="suseCreateByName" type="text" placeholder="必填, 请输入姓名" style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
          <n-select v-model:value="suseCreateByGroup" placeholder="必填, 请选择组" style="margin-bottom: 10px; max-width: 200px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select v-model:value="suseCreateBySex" placeholder="必填, 请选择性别" style="margin-bottom: 10px; max-width: 150px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input v-model:value="suseCreateByPhone" type="text" placeholder="必填, 请输入手机号码" style="margin-bottom: 10px; max-width: 220px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input v-model:value="suseCreateByEmail" type="text" placeholder="必填, 请输入工作邮箱" style="margin-bottom: 10px; max-width: 300px"
                   disabled/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input v-model:value="suseCreateByArchgroup" type="text" placeholder="必填, 请输入组织架构" style="margin-bottom: 10px;" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">创建时间</div>
          <n-date-picker type="datetime" clearable disabled placeholder="创建时间" style="max-width: 300px;"/>
          <div style="font-size: 12pt; font-weight: bold;">最后一次修改时间</div>
          <n-date-picker type="datetime" clearable disabled placeholder="最后一次修改时间" style="max-width: 300px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onDetailModalOk" type="primary">关&nbsp;闭</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改成员"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input v-model:value="updateName" type="text" placeholder="请输入更新后的姓名" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">工号</div>
          <n-input v-model:value="updateJobNumber" type="text" placeholder="请输入更新后的工号" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">组</div>
<!--          <n-select v-model:value="updateGroup" placeholder="请输入更新后的组" style="margin-bottom: 10px; max-width: 200px"/>-->
          <n-input v-model:value="updateGroup" placeholder="请输入更新后的组" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">性别</div>
          <n-select v-model:value="updateSex" :options="roleSelectOptions" placeholder="请输入更新后的性别" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">手机号码</div>
          <n-input v-model:value="updatePhone" type="text" placeholder="请输入更新后的手机号码" style="margin-bottom: 10px; max-width: 220px"/>
          <div style="font-size: 12pt; font-weight: bold;">工作邮箱</div>
          <n-input v-model:value="updateEmail" type="text" placeholder="请输入更新后的工作邮箱" style="margin-bottom: 10px; max-width: 300px"/>
          <div style="font-size: 12pt; font-weight: bold;">组织架构</div>
          <n-input v-model:value="updateArchGroup" type="text" placeholder="请输入更新后的组织架构" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onModifyModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onModifyModalOk" type="primary">修&nbsp;改</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal
        v-model:show="isShowDeleteModal"
        :mask-closable="false"
        preset="dialog"
        title="危险操作"
        content="这是一个危险的操作，你确认要删除这个数据吗？"
        positive-text="确认"
        negative-text="取消"
        @positive-click="onPositiveClick"
        @negative-click="onNegativeClick"
    />
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {getCurrentInstance, h, onMounted, reactive, ref} from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, PlusOutlined, DeleteOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance();
const dialog = useDialog()
const message = useMessage()

let accounts = ref([])
let nowRow = ref()
let now_Row = ref()
let row_now = ref()

let memberName = ref("");
let memberNo = ref("");
let memberGroup = ref("");
let memberPhone = ref("");
let memberEmail = ref("");
let memberArchGroup = ref("");

let useCreateByName = ref("")
let useCreateByNo = ref("")
let useCreateByGroup = ref("")
let useCreateBySex = ref("")
let useCreateByPhone = ref("")
let useCreateByEmail = ref("")
let useCreateByArchGroup = ref("")

let updateName = ref("")
let updateJobNumber = ref("")
let updateGroup = ref("")
let updateSex = ref("")
let updatePhone = ref("")
let updateEmail = ref("")
let updateArchGroup = ref("")

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDetailModal = ref(false);
let isShowDeleteModal = ref(false);

const checkedRowKeysRef = ref([]);

let roleSelectOptions  = [
  {
    label: "请选择性别",
    value: ""
  }, {
    label: "男",
    value: "男"
  }, {
    label: "女",
    value: "女"
  },
]

onMounted(() => {
  handleSearchAll()
})

function onAddModalAfterLeave() {

}

function onModifyModalAfterLeave() {

}

function onDetailModalAfterLeave() {

}

function onAddModalOk() {
  isShowAddModal.value =false;

  let name = useCreateByName.value
  let job_number = useCreateByNo.value
  let group = useCreateByGroup.value
  let sex = useCreateBySex.value
  let phone = useCreateByPhone.value
  let email = useCreateByEmail.value
  let arch_group = useCreateByArchGroup.value

  proxy.$axios.put("/api/account/create", {
    create_name: name,
    create_job_number: job_number,
    create_group: group,
    create_sex: sex,
    create_phone: phone,
    create_email: email,
    create_arch_group: arch_group,
  }).then( (res) => {
    if (res.status === 200) {
      console.log("创建成功")
      handleSearchAll()
    }
  }).catch(err => {
    console.log(err)
  })
}

function onAddModalFailed() {
  isShowAddModal.value =false;
}

function onDetailModalOk() {
  isShowDetailModal.value = false;
}
function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;

  let uid = now_Row["uid"]
  console.log(uid)
  let updateByName = updateName.value
  let updateByJobNumber = updateJobNumber.value
  let updateByGroup = updateGroup.value
  let updateByPhone = updatePhone.value
  let updateByEmail = updateEmail.value
  let updateBySex = updateSex.value
  let updateByArchGroup = updateArchGroup.value

  proxy.$axios.put("/api/account/" + uid, {
    name: updateByName,
    job_number: updateByJobNumber,
    group: updateByGroup,
    phone: updateByPhone,
    email: updateByEmail,
    sex: updateBySex,
    arch_group: updateByArchGroup,
  }).then( (res) => {
    if (res.status === 200) {
      console.log("创建成功！")
      message.success("数据更新成功！")
      handleSearchAll()
    }
  }).catch(err => {
    console.log(err)
    message.success("数据更新失败！")
  })
}

function handleSearchButtonClicked() {
  let name = memberName.value
  let no = memberNo.value
  let group = memberGroup.value
  let phone = memberPhone.value
  let email = memberEmail.value
  let sex = memberSexSelectOptions
  let archGroup = memberArchGroup.value


}

function handleSearchAll() {
  proxy.$axios.get("/api/account/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];

        data.map((item) => {
          result.push({
            "uid": item["uid"],
            "key": item["uid"],
            "name": item["name"],
            "job_number": item["job_number"],
            "group": item["group"],
            "phone": item["phone"],
            "email": item["email"],
            "sex": item["sex"],
            "arch_group": item["arch_group"],
            "create_time": item["create_time"],
            "update_time": item["update_time"],
          })
        });

        accounts.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
}

function handleUpdateCheckedRowKeys(rowKeys) {
  checkedRowKeysRef.value = rowKeys
  console.log(rowKeys)
}

function onPositiveClick() {

  let job_number = nowRow["job_number"]

  proxy.$axios.delete("/api/account/useJobNumberDelete", {
    params: {
      job_number: job_number,
    }
  }).then(c => {
    if (c.status === 200) {
      handleSearchAll()
      message.success("数据删除成功");
    }
  }).catch(e => {
    message.success("数据删除失败");
    console.log(e)
  })
}

function handleAddButtonClicked() {
  isShowAddModal.value = true;
}

function handleBatchEmptyButtonClicked() {
  memberName.value = ""
  memberNo.value = ""
  memberGroup.value = ""
  memberPhone.value = ""
  memberEmail.value = ""
  memberArchGroup.value = ""
  memberArchGroup.value = ""
}

function handleBatchDeleteButtonClicked() {
  dialog.warning({
    title: "即将执行批量删除动作!",
    content: "即将删除" + checkedRowKeysRef.value.length + "条数据, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick: () => {

      console.log(checkedRowKeysRef.value)

      let is_delete = checkedRowKeysRef.value
      console.log(is_delete[0])
      console.log(typeof is_delete)
      proxy.$axios.delete("/api/account/Remove", {
        data: {
          data: is_delete,
        }
      }).then(r => {
        if ( r.status === 200) {
          handleSearchAll()
          message.success("已删除" + " " + is_delete.length + " " + "条数据 !")
        }
      }).catch(err => {

      })

    },
  })
}

const memberSexSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "男",
    value: "男"
  }, {
    label: "女",
    value: "女"
  },
]

let columns = [{
  type: "selection",
  fixed: "left",
}, {
  title: "姓名",
  key: "name",
  fixed: "left",
  width: 100
}, {
  title: "工号",
  key: "job_number",
  width: 120
}, {
  title: "组",
  key: "group",
  width: 100,
  fixed: "left"
},
  {
    title: "手机号码",
    key: "phone",
    width: 150
  }, {
    title: "工作邮箱",
    key: "email",
    width: 200
  },
  {
    title: "性别",
    key: "sex",
    width: 100
  },
  {
    title: "组织架构",
    key: "arch_group",
    resizable: true,
    width: 200
  },

  {
    title: "创建时间",
    key: "create_time",
    width: 240
  }, {
    title: "最后一次修改时间",
    key: "update_time",
    width: 240
  }, {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          TableOperationAreaButtonGroup, {
            isShowDetail: false,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
              isShowDetailModal.value = true;
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true;

              now_Row = row
            },
            onDeleteButtonClicked: () => {
              isShowDeleteModal.value = true
              nowRow = row
            },
          }
      );
    },
    fixed: "right",
    width: 150
  },
];

const pagination = reactive({
  page: 1,
  pageSize: 10,
  showSizePicker: true,
  pageSizes: [5, 10, 20, 50, 100],
  onChange: (page) => {
    pagination.page = page;
  },
  onUpdatePageSize: (pageSize) => {
    pagination.pageSize = pageSize;
    pagination.page = 1;
  }
})


</script>


<style scoped>
.op-area {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
}

.member-mgmt-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>