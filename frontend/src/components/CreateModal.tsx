import React, { useState } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, TextField, Stack, Button, FormControl, Select, MenuItem, InputLabel } from '@mui/material';
import { MRT_ColumnDef } from 'material-react-table';

interface CreateModalProps<T extends Record<string, any>> {
  columns: MRT_ColumnDef<T>[];
  onClose: () => void;
  onSubmit: (values: T) => void;
  open: boolean;
}

const CreateModal = <T extends Record<string, any>,>({ open, columns, onClose, onSubmit }: CreateModalProps<T>) => {
  const [values, setValues] = useState<any>(() =>
    columns.reduce((acc, column) => {
      acc[column.accessorKey ?? ''] = column.accessorKey === 'enum' ? 'Active' : '';
      return acc;
    }, {} as any),
  );

  const handleSubmit = () => {
    onSubmit(values);
    onClose();
  };

  return (
    <Dialog open={open}>
      <DialogTitle textAlign="center">Create New</DialogTitle>
      <DialogContent>
        <form onSubmit={(e) => e.preventDefault()}>
          <Stack
            sx={{
              width: '100%',
              minWidth: { xs: '300px', sm: '360px', md: '400px' },
              gap: '1.5rem',
            }}
          >
            {columns.filter((column) => column.header !== "ID").map((column, idx) => (
              column.accessorKey === 'enum' ?
                <FormControl key={column.accessorKey}>
                  <InputLabel>{column.header}</InputLabel>
                  <Select
                    variant='standard'
                    label={column.header}
                    name={column.accessorKey}
                    value={values[column.accessorKey]}
                    onChange={(e) =>
                      setValues({
                        ...values,
                        [e.target.name]: e.target.value,
                      })
                    }
                  >
                    <MenuItem value="Active">Active</MenuItem>
                    <MenuItem value="Not Active">Not Active</MenuItem>
                  </Select>
                </FormControl>
                :
                <TextField
                  variant='standard'
                  key={idx}
                  label={column.header}
                  name={typeof column.accessorKey === 'string' ? column.accessorKey : ''}
                  onChange={(e) => setValues({ ...values, [e.target.name]: e.target.value })}
                />
            ))}
          </Stack>
        </form>
      </DialogContent>
      <DialogActions sx={{ p: '1.25rem' }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button color="secondary" onClick={handleSubmit} variant="contained">
          Create New
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default CreateModal;